# MP3 player 
## Description 
 The problem that was initially proposed was to design a mp3 player using a microcontroller or a microprocessor of our choice. We decided that are going to develop a prototype composed by a microcontroller(Arduino Mega) and a microcomputer(RaspberryPi). To communicate along the two devices we'll be using Python, just to simplify future problems. 
In this repository is all the source code and all the dependencies of the project.

## Python libraries
* To play the music we use `Vlc` or better known as `pyvlc`
* To manage the intervals of time better `time`
* To use the GPIO ports of the raspberry pi `RPi.GPIO` 
* To get random numbers `random`
* For our interface we use `pygame 2.0.1` and `pygame_menu 4.1`  
* To communicate via serial communication with an Arduino Mega `serial` 

## Harware
Main.py is the one that you need to run to check this project. You need:
* Raspberry Pi 4
* 5 buttons
* 5 1k resistor
* Rotatory encoder
* Joystick
* DHT11 temperature sensor
* Arduino Mega 2560

## Bugs
* VLC not showing song information properly.
* Pygame not changing font size.
