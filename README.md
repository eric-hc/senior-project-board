# Battleship Board

This repository contains the necessary pieces to deploy this app on a Raspberry Pi given that the board has all the correct IO needed for our Battleship game. Check out the Wiki for more information about the project.
## Prerequisites
 * Raspberry Pi 3 
 * LEDs, resistors, etc.
 
## Test API calls
  * GET `ec2-34-195-93-38.compute-1.amazonaws.com:3001/test2`
  * POST `ec2-34-195-93-38.compute-1.amazonaws.com:3001/test`
  
## Configuring I2C
  * Run `sudo raspi-config` 
  * Interfacing Options
  * P5 I2C
  * Select Yes, Yes
  * Reboot with `sudo reboot`
  * Test with `sudo i2cdetect -y 1`