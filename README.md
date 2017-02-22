# Battleship Board

This repository contains the necessary pieces to deploy this app on a Raspberry Pi given that the board has all the correct IO needed for our Battleship game. Check out the Wiki for more information about the project.

## Prerequisites
 * Raspberry Pi 3 
 * HT16K33 LED Matrix
 * MCP23017 port expander 
 * LEDs, reed switches, resistors, etc.
 
## API calls
  * `/ships` returns a list of coordinates in which the player has placed their ships
  * `/hit` turn an LED on
  
## Configuring I2C
  * Run `sudo raspi-config` 
  * Interfacing Options
  * P5 I2C
  * Select Yes, Yes
  * Reboot with `sudo reboot`
  * Test with `sudo i2cdetect -y 1`