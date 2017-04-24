# Battleship Board

This repository contains the necessary pieces to deploy this app on a Raspberry Pi given that the board has all the correct IO needed for our Battleship game. Check out the Wiki for more information about the project.

## Prerequisites
 * Raspberry Pi 3 
 * HT16K33 LED Matrix
 * MCP23017 port expander 
 * LEDs, reed switches, etc.
  
## Configuring I2C
  * Run `sudo raspi-config` 
  * Select `5 Interfacing Options`
  * Select `P5 I2C`
  * Select Yes, Yes
  * Select Finish
  * Reboot with `sudo reboot`
  * Test with `sudo i2cdetect -y 1`
  * Try this `sudo apt-get install python-smbus`
  
## Add Adafruit LED Matrix dependency
  
## Running the server manually
 * Open Terminal
 * `cd` into the correct folder, `/api`
 * `node server.js`