#!/usr/bin/env python3
# NeoPixel 库标准测试例程
# 作者: Tony DiCola
# 说明：在灯带中展示各种花式控制
#
#翻译和注释：01studio （www.01studio.org）

import time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED灯带配置:
LED_COUNT = 30        # LED灯珠数量.
LED_PIN = 18          # 树莓派GPIO引脚 (18 使用 PWM).
#LED_PIN = 10        # 树莓派GPIO引脚 (10 使用 SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED信号频率（Hz） (通常是 800khz)
LED_DMA = 10          # 直接存储器存取通道用来产生信号(尝试10)
LED_BRIGHTNESS = 255  #  0：最暗，255：最亮。
LED_INVERT = False    # True：信号反转 (when using NPN transistor level shift)
LED_CHANNEL = 0       #  设置 1 ：为 GPIOs 13, 19, 41, 45 or 53


# 定义LED动作函数.

def colorWipe(strip, color, wait_ms=50):
    """逐个LED灯珠点亮"""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChase(strip, color, wait_ms=50, iterations=10):
    """电影院灯光风格"""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, color)
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


def wheel(pos):
    """生成跨越0-255个位置的彩虹颜色."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


def rainbow(strip, wait_ms=20, iterations=1):
    """绘制彩虹，淡出所有像素一次."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def rainbowCycle(strip, wait_ms=20, iterations=5):
    """绘制均匀分布在所有像素的彩虹。."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms / 1000.0)


def theaterChaseRainbow(strip, wait_ms=50):
    """彩虹电影院灯光风格的."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, wheel((i + j) % 255))
            strip.show()
            time.sleep(wait_ms / 1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i + q, 0)


# 主函数:
if __name__ == '__main__':

    #终端执行参数
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    #根据参数构建灯带对象.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)

    # 灯带初始化
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            #逐个点亮
            print('Color wipe animations.')
            colorWipe(strip, Color(255, 0, 0))  # 红色
            colorWipe(strip, Color(0, 255, 0))  # 绿色
            colorWipe(strip, Color(0, 0, 255))  # 蓝色

            #电影院模式
            print('Theater chase animations.')
            theaterChase(strip, Color(127, 127, 127))  # White theater chase
            theaterChase(strip, Color(127, 0, 0))  # Red theater chase
            theaterChase(strip, Color(0, 0, 127))  # Blue theater chase

            #彩虹模式
            print('Rainbow animations.')
            rainbow(strip)
            rainbowCycle(strip)
            theaterChaseRainbow(strip)

    #指令中断：Ctrl+C
    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
