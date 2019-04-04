import math
import re

class printer:
    numberNozze = 2
    distanceBetweenNozze = 50
    future_position_one = [0,0]
    future_position_two = [600,600]
    distance = 10
    X_distance = 0
    Y_distance = 0
    Gcode_1 = ""
    Gcode_2 = ""
    line_Num_One = 4
    line_Num_Two = 4
    def __init__(self,numberNozze):
        print("Start")
    
    def getGcode(self,line_Num_One,line_Num_Two):
        file1 = "Gcode/box1_ver1.txt"
        file2 = "Gcode/box2_ver1.txt"
        fileGcode1 = open(file1)
        fileGcode2 = open(file2)
        Line1 = fileGcode1.readlines()
        Line2 = fileGcode2.readlines()
        self.Gcode_1 = Line1[line_Num_One]
        self.Gcode_2 = Line2[line_Num_Two]
        #print(self.Gcode_1)
        #print(self.Gcode_2)
    def num(self,s):
        try:
            return int(s)
        except ValueError:
            return float(s)
    def getPosition(self):
        self.getGcode(self.line_Num_One,self.line_Num_Two)
        Gcode1 = re.split("\s",self.Gcode_1)
        Gcode2 = re.split("\s",self.Gcode_2)
        #print(Gcode1)
        #print(Gcode2)
        if len(Gcode1) > 3 and (Gcode1[0] == "G1" or Gcode1[0] == "G0"):
            if Gcode1[1][0] == 'X':
                self.future_position_one[0] = self.num(Gcode1[1][1:])
            if Gcode1[2][0] == 'Y':
                self.future_position_one[1] = self.num(Gcode1[2][1:])
        if len(Gcode2) > 3 and (Gcode2[0] == "G1" or Gcode2[0] == "G0"):
            if Gcode2[1][0] == 'X':
                self.future_position_two[0] = self.num(Gcode2[1][1:])
            if Gcode2[2][0] == 'Y':
                self.future_position_two[1] = self.num(Gcode2[2][1:])
        print(self.future_position_one)
        print(self.future_position_two)
    def caculateDistance(self):
        #caculate distance between future_position_one and future_position_two
        #d = sqrt(x^2 +y^2)
        self.getPosition()
        self.X_distance = self.future_position_one[0] - self.future_position_two[0]
        self.Y_distance = self.future_position_one[1] - self.future_position_two[1]
        self.distance = math.sqrt((self.X_distance*self.X_distance+self.Y_distance*self.Y_distance))
        print("Distance: "+ str(self.distance))
        f=open("Gcode/distance.txt","a")
        f.write(str(self.distance)+"\n")
        f.close()
    def sendGcodeToMachine(self):
        #Sending
        print("Send "+ self.Gcode_1 +" to machine 1")
        print("Send "+ self.Gcode_2 +" to machine 2")
        #check respond from machine 1
        #resFromOne = input("Res from one: ")
        resFromOne = "ok"
        #check respond from machine 2
        #resFromTwo = input("Res from two: ")
        resFromTwo = "ok"
        #if respond OK:
        #update new Gcode to file data1 and data2
        if resFromOne == "ok":        
            self.line_Num_One = self.line_Num_One + 1
        if resFromTwo == "ok":
            self.line_Num_Two = self.line_Num_Two + 1
        print("update")
        print("Current machine one line: " + str(self.line_Num_One))
        print("Current machine two line: " + str(self.line_Num_Two))

    def control(self):
        self.caculateDistance()
        if self.distance <= self.distanceBetweenNozze:
            #stop nozze 1
            self.Gcode_1 = "M0\n"
            print(self.Gcode_1)
            #continue nozze 2
            print(self.Gcode_2)
            self.sendGcodeToMachine()
        else: 
            self.sendGcodeToMachine()
