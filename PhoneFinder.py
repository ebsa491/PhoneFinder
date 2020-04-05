#!/usr/bin/python3
# GNU Lesser General Public License (LGPL) v3.0 .
# The project has been developed by Saman Ebrahimnezhad .
# Created at Iran (IR) .
# Python 3 .

import json

class PhoneFinder:

    def __init__(self):

        # figlet used for ASCII

        icon = open('/etc/PhoneFinder/icon.txt', 'r')

        icon_contents = icon.read()

        print(icon_contents)

        icon.close()

        code = input("Enter the code: ")

        f = open("Phone_Codes.json", "r")

        jsonFile = f.read()

        parsedJson = json.loads(jsonFile)

        for x in parsedJson:
        	if code == x:
        		print(parsedJson[x])
        		break

        f.close()

def main():
    app = PhoneFinder()

if __name__ == '__main__':
    main()
