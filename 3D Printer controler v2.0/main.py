import virtualPrinter
import threading
"""printerOne = virtualPrinter.typeOnePrinter()
printerOne.connectToPrinter()
printerOne.run()
for i in range(0):
    printerOne.getGcodeFileDir("Gcode/one")
    printerOne.getGcodeLine()
    printerOne.getPositionFromGcodeRecive()
    print(printerOne.PositionFromGcodeRecive)
    a = printerOne.caculateDistanceToPoint([0,0])
    b = printerOne.checkCollision(a)
    if not b :
        printerOne.updateCurrentPosition(printerOne.PositionFromGcodeRecive)
        print("current")
        print(printerOne.currentPosition)
    printerOne.increaseOrderGcodeLine()"""
#################### Config for Printer One #############
# Name for Printer 1
nameOne = "onePrinter"
# Gcode file direction
gcodeOneDir = "Gcode/one"
# Serial connection port and baudrate
portOne = 'COM7'
baudrateOne = 115200
#=========================================================


##################### Config for printer two  ################
#Name for Printer 2
nameTwo = "twoPrinter"
# Gcode file direction
gcodeTwoDir = "Gcode/two"
# Serial connection port and baudrate
portTwo = 'COM8'
baudrateTwo = 115200

#=========================================================

onePrinter = virtualPrinter.typeOnePrinter(nameOne,gcodeOneDir,portOne,baudrateOne)
twoPrinter = virtualPrinter.typeTwoPrinter(nameTwo,gcodeTwoDir,portTwo,baudrateTwo)

onePrinter.getFirstFriendPrinter(twoPrinter)
twoPrinter.getFirstFriendPrinter(onePrinter)

#Connect One Printer
onePrinter.connectToPrinter()

#Connect Two Printer
twoPrinter.connectToPrinter()

# onePrinter.start()
# twoPrinter.start()

# onePrinter.join()
# twoPrinter.join()

print(threading.enumerate())