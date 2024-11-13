import sys
import random
from pyfiglet import Figlet

figlet=Figlet()
#check for invalid argument
if sys.argv[1]!="-f":
    sys.exit("Invalid usage")
fonts=figlet.getFonts()

f=sys.argv[2]
#check for invalid font
if f in fonts:
    figlet.setFont(font=f)
else:
    sys.exit("Invalid usage")
#display output
s = input("Input: \n")
print(figlet.renderText(s))

