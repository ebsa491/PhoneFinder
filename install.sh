#!/bin/bash
# GNU Lesser General Public License (LGPL) v3.0 .
# The project has been developed by Saman Ebrahimnezhad .
# Created at Iran (IR) .
# Bash .

echo -e "[\033[0;32m*\033[0m] Installing PhoneFinder..."

sudo mkdir /etc/PhoneFinder

sudo cp dist/PhoneFinder /bin/

sudo cp icon.txt /etc/PhoneFinder/

echo

echo -e "\033[0;32m Installed successfully! \033[0m"
