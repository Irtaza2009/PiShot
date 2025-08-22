---
title: "PiShot"
author: "Irtaza"
description: "A Raspberry Pi Zero 2W Camera with an LCD display, buttons, and a custom case!"
created_at: "2025-07-26"
---

### Total Time Spent: ~19 hours!

### July 25th: Research + Wiring Diagram
The plan is to make a Camera with a custom 3d case (with a tripod, grip, and viewfinder), using the Raspberry Pi Zero 2W, and the Pi camera module 3, and the ST7789 LCD, that stores the photos on an SD card, and you can view the last photo (and explore all the shoots) on the display!! It will be in the Cyber-shot form factor!!

Started by looking up all the different Pi Camera modules and comparing their results! Settled on the Camera module 3, as it has auto focus! I will be using the Pi Zero 2W as the MCU, as it is the lowest-performance MCU that supports the camera. 
Then I made a list of all the components I would need! I decided to go with a 1500mAh 3.7V LiPo battery with an MT3608 boost converter, and a TP4056 module (with protection) to charge it! (At first, I was considering a power bank or an 18650 cell, but those are too bulky!)
For the display, I will be using the ST7789 TFT-LCD. And a metal momentary push button (similar to [this](https://www.adafruit.com/product/558), but without the LED ring!) for the shutter button! And I will also place an SPDT slide switch to turn it on and off!

I decided that I won't be using a PCB, so it's easier to place all the components in the case. So I will make a wiring diagram instead! Thus, I opened up [Cirkit Designer](https://app.cirkitdesigner.com/), and got to work!! [This](https://app.cirkitdesigner.com/project/cb34b867-8320-4c2c-972f-24cbd0726ab1) is what I came up with!

<img width="3000" height="2013" alt="circuit_image (1)" src="https://github.com/user-attachments/assets/8c0cb2bf-a454-4c5b-81e3-681301218cdd" />

**Total time spent: 3.5 hours**

### July 26th: Started 3d Case Design

I began by finding and downloading 3D models of all the components I would be using. This process took a significant amount of time, as I had to search extensively to locate every part! After that, I started designing the case in Shapr3D on my iPad. I first created a rectangular base for the body, including a removable back. Next, I added a square hole in the centre for the camera module, and a hole at the top for the shutter button. The challenging part was designing a grip that could slide into the case and be removed easily. Developing the sliding mechanism took quite a while, but I think it turned out pretty cool!

<img width="285" height="427" alt="image" src="https://github.com/user-attachments/assets/cd110c81-74df-4898-acd5-777e4fd10602" />
<img width="606" height="427" alt="image" src="https://github.com/user-attachments/assets/4ad3debe-dd22-40c2-8b97-52c015f95244" />

I began by placing each component into the interior of the case, ensuring that they were properly secured. I created holes on the sides and bottom for the SD card and the USB port of the Raspberry Pi. I also made an opening in the back cover for the LCD screen and added supports for all the components. However, I did not create a hole for the USB-C port, as I was still unsure about where to place it. 

<img width="520" height="385" alt="image" src="https://github.com/user-attachments/assets/99a0b39e-65e3-422b-8b96-b6b040019c25" />
<img width="474" height="385" alt="image" src="https://github.com/user-attachments/assets/f7afa6d4-ed17-4548-8d65-b04642f0acfe" />

<img width="520" height="425" alt="image" src="https://github.com/user-attachments/assets/ed7024ea-5300-4f40-8aba-95963028e34a" />
<img width="478" height="425" alt="image" src="https://github.com/user-attachments/assets/fc9df2a5-7879-43af-b704-9b1fc7ae334f" />

**Total time spent: 7 hours**

### July 27th: Buttons + USB C port + TP4056 supports

Looked through the datasheet for [these](https://tech.alpsalpine.com/e/products/detail/SKRGAED010/) circle micro pushbuttons and noted their size, then made a cool to-size slot for them in the case!

<img width="464" height="454" alt="image" src="https://github.com/user-attachments/assets/ae0a2edd-2afa-437c-99ed-293c89fa130a" />
<img width="470" height="364" alt="image" src="https://github.com/user-attachments/assets/0ec3f5a8-b3d0-4699-aec6-0cfc5d02fd34" />
<img width="478" height="293" alt="image" src="https://github.com/user-attachments/assets/88141bc2-0f38-4adf-bcb5-248ea1174a5c" />


Then, I also made a slot for the USB-C port, and some supports for the TP4056!

<img width="513" height="300" alt="image" src="https://github.com/user-attachments/assets/b95e5e53-d03f-4943-bd9b-898d2694520d" />
<img width="564" height="399" alt="image" src="https://github.com/user-attachments/assets/7cf7fe17-e186-4c2e-bb00-3eb7cf105a50" />

**Total Time spent: 2 hours**

### July 28th: Tripod + Viewfinder

Inspired by the removable Sony viewfinder, I also decided to make one too! It will also have a sliding mechanism like the grip! I started by making an extrusion and adding the sliding mechanism, then I made a separate rectangle body, with a rectangle hole in the middle (this will be the viewfinder). I then fillet/chamfered it to look more trapezium-ish, like a real viewfinder. And finally, I also added some nice rounded supports to rest the eye on! These were the final results!!

<img width="264" height="202" alt="image" src="https://github.com/user-attachments/assets/bdaa236d-85d6-43ef-928d-cbd158be57eb" />
<img width="304" height="248" alt="image" src="https://github.com/user-attachments/assets/503a9167-95cc-40ec-9e1c-2ef69dca1110" />

Then I thought about adding support for standard tripods! And, of course, I think the sliding mechanism is super cool, so I built another bit of it on the bottom of the case, and then made a cube with a screw hole in it! Thankfully, I discovered Shapr3d's subtract tool, or I don't think I could have ever made the screw curve paths!! And finally rounded off the edges to make it look more polished!

<img width="306" height="255" alt="image" src="https://github.com/user-attachments/assets/05ae695a-6135-43d5-aa06-1e5e8aa951f6" />

Then I remembered I had forgotten to add space for the SPDT On/Off switch, so I added that!

<img width="145" height="97" alt="image" src="https://github.com/user-attachments/assets/4d4c5abe-a00a-485f-bb30-608b4c7e27c6" />

**Total Time spent: 3 hours**

### July 29th: Finished Design

The only thing left now was some final polishing- wait, I forgot to make space for a rechargeable battery!! So I imported a model of an 18650 cell, and tried to make space for it! But I couldn't :(. So finally I split my case (front, back, grip, everything) into two parts, increased its height by 5mm, and then joined it once again! So now my case was 5mm taller, and I could fit the battery inside too! And then I had to move around all the slots like front buttons, screen, camera hole, etc, around to centre them again and make them look nice!

<img width="430" height="379" alt="image" src="https://github.com/user-attachments/assets/48c26c1a-e7cd-49ee-bbdf-468fa7159d4c" />
<img width="382" height="379" alt="image" src="https://github.com/user-attachments/assets/0203dd44-053e-4d89-bec9-d0dd035a015f" />

<img width="468" height="442" alt="image" src="https://github.com/user-attachments/assets/7d050b3b-c135-4082-9f34-17d2d82d5d1b" />
<img width="514" height="442" alt="image" src="https://github.com/user-attachments/assets/d11e9813-90ac-4d53-b4ab-347e53442fbc" />

And then I also added some text to the front of the camera, for _personalisation_!

<img width="398" height="277" alt="image" src="https://github.com/user-attachments/assets/961ffaab-5933-4ffc-a89a-37eb2c37df23" />

Final 3d design!!

<img width="474" height="407" alt="image" src="https://github.com/user-attachments/assets/352f30d1-cc85-4969-8895-ab5d76c42ac4" />
<img width="420" height="407" alt="image" src="https://github.com/user-attachments/assets/0605512e-7c4c-4b2d-bf0e-a7fdc5f751d8" />

**Total Time spent: 2.5 hours**

### July 30th: Made firmware

Got to work on coding the firmware for the Pi! I have never before used a Pi Zero 2w, but it was super easy to code for it because, well, it's a full Linux computer! So no flashing or stuff, I just have to make a Python file and add it to run on boot!

Right now, I randomly assigned the GPIO pins in the code because I don't know what pin I might end up using for what. The script ~~should~~ will: display a splash screen, wait for shutter button press, capture image from camera, and save it to SD card with a timestamped filename!

**Total Time spent: 1 hour**

### IRL Building!!

### August 20th: Finished buidling prototype

All of the parts arrived today except for the Pi Zero W camera ribbon cable and the 3d case. So I decided to start and make a breadboard prototype to make sure everything works, and also just to make everything with the camera functionality, so I only need to connect the camera when the cable arrives!

First, I flashed an SD card with Pi OS, with SSH enabled, and put that into the Pi Zero 2W! Then I SSHed into it! And it was really fun! I might even have got lost playing with all the different settings and testing out the different RPi features like RPi connect c:! The interface was interesting! Then I used nano for the first time to code, and it was pretty easy to use after learning the shortcuts (though selection is pretty hard).

<img width="1978" height="1088" alt="WindowsTerminal_ovPsQCGSl1" src="https://github.com/user-attachments/assets/afde9b71-8a98-4fbd-b676-77d7b995066a" />

After that, I looked up the pin layout for the Pi Zero 2 W, attached my shutter and pushbuttons, and my OLED. The buttons worked fine, but it took a lot of time to make the LED work! And after a lot of going back and forth, debugging the LED, I found out that it was not a 128x64 SSD1306, but a 132x64 SH1106. So I downloaded its libraries, updated my code, and it started working!

Then I brought out my soldering iron and got to work soldering the power components! I think everything was correctly set up, but I didn't connect it to the Pi just yet, because I don't know what output voltage the MT3608 is set to, as I don't have a multimeter, and don't want to fry my Pi Zero 2 W.

Now I just have to wait for the Pi Zero 2 W camera ribbon cable to arrive!!

**Total time spent: 4.5 hours**
