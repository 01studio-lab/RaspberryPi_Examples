import smbus
import time
import subprocess
import sys
import os

class BMP280():

    def __init__(self,port=1):
        
        #I2C bus
        self.bus = smbus.SMBus(port)
        
        self.b1 = []
        self.dig_T1 = 0
        self.dig_T2 = 0
        self.dig_T3 = 0
        self.data = 0
        self.adc_t = 0
        self.dig_P1 = 0
        self.dig_P2 = 0
        self.dig_P3 = 0
        self.dig_P4 = 0
        self.dig_P5 = 0
        self.dig_P6 = 0
        self.dig_P7 = 0
        self.dig_P8 = 0
        self.dig_P9 = 0     

        #BMP280 address, 0x76(118)
        #Read data back from 0x88(136), 24 bytes        
        try:
            self.b1 = self.bus.read_i2c_block_data(0x76, 0x88, 24)
        except IOError:
            subprocess.call(['i2cdetect', '-y', '1'])
            flag = 1     #optional flag to signal your code to resend or something
            
    def get(self):
        self.dig_T1 = self.b1[1] * 256 + self.b1[0]
        self.dig_T2 = self.b1[3] * 256 + self.b1[2]
        if self.dig_T2 > 32767:
            self.dig_T2 -= 65536
        self.dig_T3 = self.b1[5] * 256 + self.b1[4]
        if self.dig_T3 > 32767:
            self.dig_T3 -= 65536
        
                # Pressure coefficents
        self.dig_P1 = self.b1[7] * 256 + self.b1[6]
        self.dig_P2 = self.b1[9] * 256 + self.b1[8]
        if self.dig_P2 > 32767 :
            self.dig_P2 -= 65536
        self.dig_P3 = self.b1[11] * 256 + self.b1[10]
        if self.dig_P3 > 32767 :
            self.dig_P3 -= 65536
        self.dig_P4 = self.b1[13] * 256 + self.b1[12]
        if self.dig_P4 > 32767 :
            self.dig_P4 -= 65536
        self.dig_P5 = self.b1[15] * 256 + self.b1[14]
        if self.dig_P5 > 32767 :
            self.dig_P5 -= 65536
        self.dig_P6 = self.b1[17] * 256 + self.b1[16]
        if self.dig_P6 > 32767 :
            self.dig_P6 -= 65536
        self.dig_P7 = self.b1[19] * 256 + self.b1[18]
        if self.dig_P7 > 32767 :
            self.dig_P7 -= 65536
        self.dig_P8 = self.b1[21] * 256 + self.b1[20]
        if self.dig_P8 > 32767 :
            self.dig_P8 -= 65536
        self.dig_P9 = self.b1[23] * 256 + self.b1[22]
        if self.dig_P9 > 32767 :
            self.dig_P9 -= 65536

        self.write_data()
        # BMP280 address, 0x76(118)
        # Read data back from 0xF7(247), 8 bytes
        # Pressure MSB, Pressure LSB, Pressure xLSB, Temperature MSB, Temperature LSB
        # Temperature xLSB, Humidity MSB, Humidity LSB
        self.data = self.bus.read_i2c_block_data(0x76, 0xF7, 8)
        # Convert temperature data to 19-bits
        self.adc_t = ((self.data[3] * 65536) + (self.data[4] * 256) + (self.data[5] & 0xF0)) / 16

        # Temperature offset calculations
        self.var1 = ((self.adc_t) / 16384.0 - (self.dig_T1) / 1024.0) * (self.dig_T2)
        self.var2 = (((self.adc_t) / 131072.0 - (self.dig_T1) / 8192.0) * ((self.adc_t)/131072.0 - (self.dig_T1)/8192.0)) * (self.dig_T3)
        self.t_fine = (self.var1 + self.var2)
        self.cTemp = (self.var1 + self.var2) / 5120.0
        self.fTemp = self.cTemp * 1.8 + 32
        
                # Convert pressure and temperature data to 19-bits
        self.adc_p = ((self.data[0] * 65536) + (self.data[1] * 256) + (self.data[2] & 0xF0)) / 16
        # Pressure offset calculations
        self.var1 = (self.t_fine / 2.0) - 64000.0
        self.var2 = self.var1 * self.var1 * (self.dig_P6) / 32768.0
        self.var2 = self.var2 + self.var1 * (self.dig_P5) * 2.0
        self.var2 = (self.var2 / 4.0) + ((self.dig_P4) * 65536.0)
        self.var1 = ((self.dig_P3) * self.var1 * self.var1 / 524288.0 + ( self.dig_P2) * self.var1) / 524288.0
        self.var1 = (1.0 + self.var1 / 32768.0) * (self.dig_P1)
        self.p = 1048576.0 - self.adc_p
        self.p = (self.p - (self.var2 / 4096.0)) * 6250.0 / self.var1
        self.var1 = (self.dig_P9) * self.p * self.p / 2147483648.0
        self.var2 = self.p * (self.dig_P8) / 32768.0
        self.pressure = (self.p + (self.var1 + self.var2 + (self.dig_P7)) / 16.0) / 100        

        return [self.cTemp,self.pressure]
    
    def getTemp(self):
        self.get()
        return self.cTemp
    
    def getPressure(self):
        self.get()
        return self.pressure
    
    # Calculating absolute altitude    
    def getAltitude(self):
        return '%.2f'%(44330*(1-(self.getPressure()*100/101325)**(1/5.256)))
    
    def write_data(self):
        # BMP280 address, 0x76(118)
        # Select Control measurement register, 0xF4(244)
        #       0x27(39)    Pressure and Temperature Oversampling rate = 1
        #                   Normal mode
        self.bus.write_byte_data(0x76, 0xF4, 0x27)
        # BMP280 address, 0x76(118)
        # Select Configuration register, 0xF5(245)
        #       0xA0(00)    Stand_by time = 1000 ms
        self.bus.write_byte_data(0x76, 0xF5, 0xA0)

        time.sleep(0.3)

