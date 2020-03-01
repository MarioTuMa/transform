import math

size = 500



pixels = []
for i in range(size):
    pixels.append([])
    for j in range(size):
        pixels[i].append([255,255,255])

def line(x1,y1,x2,y2,r,g,b):
    x1 = round(x1)
    x2 = round(x2)
    y1 = round(y1)
    y2 = round(y2)
    if(x1==x2):
        for i in range(min(y1,y2),max(y1,y2)+1):
            pixels[x1][i]=[r,g,b]
        return
    if(y1==y2):
        for i in range(min(x1,x2),max(x1,x2)+1):
            pixels[i][y1]=[r,g,b]
        return
    m = (y1-y2)/(x1-x2)
    #print(m)
    if(abs(m)<1):
        if(x1>x2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(x1,x2+1):
            pixels[i][y1+shift]=[r,g,b]
            extra += m
            shift=round(extra)
    if(abs(m)>1):
        m = 1/m
        if(y1>y2):
            line(x2,y2,x1,y1,r,g,b)
            return
        extra = 0
        shift = 0

        for i in range(y1,y2+1):
            pixels[x1+shift][i]=[r,g,b]
            extra += m
            shift=round(extra)

def matrixMult(a,b):
    for i in range(len(b)):
        temp = []
        for j in range(len(a)):
            sum = 0
            for k in range(len(a[0])):
                sum+=a[k][j]*b[i][k]
            temp.append(sum)
        b[i] = temp
    return b

def matrixPrint(a):
    for i in range(len(a[0])):
        stri = ""
        for j in range(len(a)):
            stri+=str(a[j][i])+" "
        print(stri)
    print("")

def altitude(p1x,p1y,p2x,p2y,p3x,p3y,r,g,b):
    m23 = (p3y-p2y)/(p3x-p2x)

    Dx = (p2y-p1y-m23*p2x-p1x/m23)/(-m23-1/m23)
    Dy = p2y+m23*(Dx-p2x)
    Dx = int(Dx)
    Dy = int(Dy)
    lineMatrix.append([p1x,p1y,0,1])
    lineMatrix.append([Dx,Dy,0,1])
    crosshair(Dx,Dy,5,255,0,0)



def crosshair(x1,y1,radius,r,g,b):
    lineMatrix.append([x1-radius,y1,0,1])
    lineMatrix.append([x1+radius,y1,0,1])
    lineMatrix.append([x1,y1-radius,0,1])
    lineMatrix.append([x1,y1+radius,0,1])


def median(p1x,p1y,p2x,p2y,p3x,p3y,r,g,b):
    lineMatrix.append([p1x,p1y,0,1])
    lineMatrix.append([int((p2x+p3x)/2),int((p2y+p3y)/2),0,1])
    crosshair(int((p2x+p3x)/2),int((p2y+p3y)/2),5,255,0,0)

def circle(centerx,centery,pointx,pointy):
    lineMatrix = []
    rotAngle = math.pi/720
    rotMatrix = [
    [math.cos(rotAngle),math.sin(rotAngle),0,0],
    [-math.sin(rotAngle),math.cos(rotAngle),0,0],
    [0,0,1,0],
    [-centerx*math.cos(rotAngle)+centery*math.sin(rotAngle)+centerx,-centerx*math.sin(rotAngle)-centery*math.cos(rotAngle)+centery,0,1]]
    lineMatrix.append([pointx,pointy,0,1])
    lineMatrix.append([pointx,pointy,0,1])

    for i in range(1440):
        matrixDraw(lineMatrix)
        # if(i%360==0):
        #     print("Multiplied line matrix that is actually a dot by rot matrix "+str(i)+" times")
        #     matrixPrint(lineMatrix)

        matrixMult(rotMatrix,lineMatrix)
        matrixPrint(lineMatrix)
    matrixDraw(lineMatrix)


def matrixDraw(lineMatrix):
    for i in range(len(lineMatrix)):
        if(i%2==0):
            line(lineMatrix[i][0],lineMatrix[i][1],lineMatrix[i+1][0],lineMatrix[i+1][1],0,0,0)

def matrixClear():

    lineMatrix=[]

def ident():
    transformMatrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

def rotz(deg):
    rotAngle = deg/180 * math.pi
    rotMatrix = [
    [math.cos(rotAngle),math.sin(rotAngle),0,0],
    [-math.sin(rotAngle),math.cos(rotAngle),0,0],
    [0,0,1,0],
    [0,0,0,1]]
    transformMatrix = matrixMult(rotMatrix,transformMatrix)

def roty(deg):
    rotAngle = deg/180 * math.pi
    rotMatrix = [
    [math.cos(rotAngle),0,-math.sin(rotAngle),0],
    [0,1,0,0],
    [math.sin(rotAngle),0,math.cos(rotAngle),0],
    [0,0,0,1]]
    transformMatrix = matrixMult(rotMatrix,transformMatrix)

def rotx(deg):
    rotAngle = deg/180 * math.pi
    rotMatrix = [
    [1,0,0,0],
    [0,math.cos(rotAngle),math.sin(rotAngle),0],
    [0,-math.sin(rotAngle),math.cos(rotAngle),0,0],
    [0,0,0,1]]
    transformMatrix = matrixMult(rotMatrix,transformMatrix)

def translateMatrix(a,b,c):
    tMatrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[a,b,c,1]]
    transformMatrix = matrixMult(tMatrix,transformMatrix)

def dilate(x,y,z):
    dMatrix = [[x,0,0,0],[0,y,0,0],[0,0,z,0],[0,0,0,1]]
    transformMatrix = matrixMult(dMatrix,transformMatrix)

def applyM():
    lineMatrix = matrixMult(transformMatrix,lineMatrix)

def addLine(x1,y1,z1,x2,y2,z2):
    lineMatrix.append([x1,y1,z1,1])
    lineMatrix.append([x2,y2,z2,1])

def drawlines():
    i = 0
    print(lineMatrix)
    while(i<len(lineMatrix)):
        line(lineMatrix[i][0],lineMatrix[i][1],lineMatrix[i][0],lineMatrix[i+1][1],0,0,0)
        i+=2

def display(name):
    drawlines()
    fout = open(name,"w")
    fout.write("P3\n"+str(size)+" "+str(size)+"\n255\n")
    for i in range(size):
        for j in range(size):
            fout.write(str(pixels[i][j][0])+" "+str(pixels[i][j][1])+" "+str(pixels[i][j][2])+" ")

        fout.write("\n")
    print("The image file is "+name)
    fout.close()

def readScript(filename):
    displaycount = 0
    fin = open(filename,"r")
    coms = fin.read()
    coms = coms.split("\n")
    print(coms)
    while(len(coms)>0):
        print(len(coms),coms[0])
        print(lineMatrix)
        if(coms[0]=="line"):
            coms[1]=coms[1].split(" ")
            addLine(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]),int(coms[1][3]),int(coms[1][4]),int(coms[1][5]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="display"):
            display("pic"+str(displaycount)+".ppm")
            displaycount+=1
            coms.pop(0)
        elif(coms[0]=="ident"):
            ident()
            coms.pop(0)
        elif(coms[0]=="scale"):
            coms[1]=coms[1].split(" ")
            dilate(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="move"):
            coms[1]=coms[1].split(" ")
            translateMatrix(int(coms[1][0]),int(coms[1][1]),int(coms[1][2]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="rotate"):
            coms[1]=coms[1].split(" ")
            if(coms[1][0]=="z"):
                rotz(int(coms[1][1]))
            if(coms[1][0]=="y"):
                roty(int(coms[1][1]))
            if(coms[1][0]=="x"):
                rotx(int(coms[1][1]))
            coms.pop(0)
            coms.pop(0)
        elif(coms[0]=="apply"):
            applyM()
            coms.pop(0)
        elif(coms[0]=="save"):

            display(coms[1])

            coms.pop(0)
            coms.pop(0)
            print(coms)
        else:
            coms.pop(0)

lineMatrix = []
transformMatrix = []



readScript("script")
