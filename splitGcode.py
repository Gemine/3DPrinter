sourcefile = "box_ver1.gcode"
file1 = "box1_ver1.txt"
file2 = "box2_ver1.txt"

f = open(sourcefile, "r")
flag = 0
f1 = open(file1, "w")
f1.write("")
f2 = open(file2, "w")
f2.write("")

for x in f:
        if x[0:2] == 'T0':
                #switch to copy to file box1
                flag = 1
        elif x[0:2] == 'T1':
                #switch to copy to file box2
                flag = 2
        else:
                pass

        if flag == 1:
                # copy to box 1
                f1 = open(file1, "a")
                f1.write(x)
                print(x)
                f1.close
        elif flag == 2:
                # copy to box2
                f2 = open(file2, "a")
                f2.write(x)
                f2.close
        else:
                pass
