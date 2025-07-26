---
title: "PiShot"
author: "Irtaza"
description: "A Raspberry Pi Zero 2W Camera with an LCD display, buttons, and a custom case!"
created_at: "2025-07-26"
---

### July 25th: Research + Wiring Diagram
The plan is to make a Camera with a custom 3d case (with a tripod, grip, and viewfinder), using the Raspberry Pi Zero 2W, and the Pi camera module 3, and the ST7789 LCD, that stores the photos on an SD card, and you can view the last photo (and explore all the shoots) on the display!! It will be in the Cyber-shot form factor!!

Started by looking up all the different Pi Camera modules and comparing their results! Settled on the Camera module 3, as it has auto focus! I will be using the Pi Zero 2W as the MCU, as it is the lowest-performance MCU that supports the camera. 
Then I made a list of all the components I would need! I decided to go with a 1500mAh 3.7V LiPo battery with an MT3608 boost converter, and a TP4056 module (with protection) to charge it! (At first, I was considering a power bank or an 18650 cell, but those are too bulky!)
For the display, I will be using the ST7789 TFT-LCD. And a metal momentary push button (similar to [this](https://www.adafruit.com/product/558), but without the LED ring!) for the shutter button! And I will also place an SPDT slide switch to turn it on and off!

I decided that I won't be using a PCB, so it's easier to place all the components in the case. So I will make a wiring diagram instead! Thus, I opened up [Cirkit Designer](https://app.cirkitdesigner.com/), and got to work!! This is what I came up with!

<img width="3000" height="2114" alt="circuit_image" src="https://github.com/user-attachments/assets/a3ad78c9-99e0-4964-ba3e-49aed0464589" />

**Total time spent: 3.5 hours**
