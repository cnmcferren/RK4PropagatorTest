import math

def GetError(actualValue,rk4Value):
    error = abs((actualValue - rk4Value)/actualValue)
    return error * 100.0

def GetDelta(actualCoord,rk4Coord):
    xelem = (float(actualCoord[0]) - float(rk4Coord[0]))**2
    yelem = (float(actualCoord[1]) - float(rk4Coord[1]))**2
    zelem = (float(actualCoord[2]) - float(rk4Coord[2]))**2

    delta = math.sqrt(xelem + yelem + zelem)

    return delta

rk4File = open('Masters/RK4_Master.csv','r')
actualFile = open('Masters/Actual_Master.csv','r')

errorFile = open('Masters/Error_Cartesian.csv','w')

rk4Lines = rk4File.readlines()
actualLines = actualFile.readlines()

deltas = []
for i in range(len(actualLines)):
    rk4Line = rk4Lines[i]
    actualLine = actualLines[i]

    rk4Line = rk4Line.split(',')
    actualLine = actualLine.split(',')

    time = actualLine[0]

    actualCoord = (float(actualLine[1]),float(actualLine[2]),float(actualLine[3]))
    rk4Coord = (float(rk4Line[1]),float(rk4Line[2]),float(rk4Line[3]))

    xErr = GetError(actualCoord[0],rk4Coord[0])
    yErr = GetError(actualCoord[1],rk4Coord[1])
    zErr = GetError(actualCoord[2],rk4Coord[2])
    delta = GetDelta(actualCoord,rk4Coord)
    deltas.append(delta)
    
    errorFile.write(str(time) + ',')
    errorFile.write(str(xErr) + ',')
    errorFile.write(str(yErr) + ',')
    errorFile.write(str(zErr) + ',')
    errorFile.write(str(delta) + '\n')

rk4File.close()
actualFile.close()
errorFile.close()

#For Spherical
rk4File = open('Masters/RK4_Master_Spherical.csv','r')
actualFile = open('Masters/Actual_Master_Spherical.csv','r')

errorFile = open('Masters/Error_Spherical.csv','w')

rk4Lines = rk4File.readlines()
actualLines = actualFile.readlines()

for i in range(len(actualLines)):
    R = 6371000 #Average radius of Earth
    
    rk4Line = rk4Lines[i]
    actualLine = actualLines[i]

    rk4Line = rk4Line.split(',')
    actualLine = actualLine.split(',')

    time = actualLine[0]
    dist = deltas[i]
    
    #Calculate Great Circle distance
    alpha = math.asin((dist/(2*R**2))*math.sqrt(4*R**2 - dist**2))
    gcDist = R * alpha

    actualCoord = (float(actualLine[1]),float(actualLine[2]),float(actualLine[3]))
    rk4Coord = (float(rk4Line[1]),float(rk4Line[2]),float(rk4Line[3]))

    rhoErr = GetError(actualCoord[0],rk4Coord[0])
    thetaErr = GetError(actualCoord[1],rk4Coord[1])
    phiErr = GetError(actualCoord[2],rk4Coord[2])
    
    errorFile.write(str(time) + ',')
    errorFile.write(str(rhoErr) + ',')
    errorFile.write(str(thetaErr) + ',')
    errorFile.write(str(phiErr) + ',')
    errorFile.write(str(gcDist) + '\n')

rk4File.close()
actualFile.close()
errorFile.close()

