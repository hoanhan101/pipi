#!/bin/sh

#
# install_requirements.sh - Install dependencies for the project 
# Author: Hoanh An (hoanhan@bennington.edu)
# Date: 05/19/18
#
# Usage:
#   ./install_requirements
#

sudo apt-get update
sudo apt-get install git
git clone https://github.com/hoanhan101/pipi.git
cd pipi
pip3 install -r requirements.txt

echo "Installed successfully"
