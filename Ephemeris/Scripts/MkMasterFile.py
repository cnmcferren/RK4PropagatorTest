# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 17:34:23 2019

@author: Supreme
"""

import matplotlib.pyplot as plt
import copy
import math

def GetDate(lines):
    dateLine = lines[22]
    date = float(dateLine[61:83])
    
    return date
    
def GetEphemeris(lines):
    ephLine = lines[26]
    ephLineParsed = ephLine.split(' ')
    
    x = float(ephLineParsed[1])
    y = float(ephLineParsed[2])
    z = float(ephLineParsed[3])
    
    xdot = float(ephLineParsed[4])
    ydot = float(ephLineParsed[5])
    zdot = float(ephLineParsed[6])
    
    return [x,y,z,xdot,ydot,zdot]
    
if __name__ == '__main__':
    
    i = 1

    actualData = []
    rk4Data = []

    while i < 18:
        
        #Parsing real data
        filename = 'Actual/' + str(i) + '.e'
        ephFile = open(filename,'r')
    
        lines = ephFile.readlines()

        ephemeris = GetEphemeris(lines)
        date = GetDate(lines)
    
        ephemeris.append(date)
    
        actualData.append(copy.copy(ephemeris))
        
        #Parsing RK4 data
        filename = 'Rk4th/RK4th_' + str(i) + '.e'
        ephFile = open(filename,'r')
        
        lines = ephFile.readlines()
        
        ephemeris = GetEphemeris(lines)
        date = GetDate(lines)
        
        ephemeris.append(date)
        
        rk4Data.append(ephemeris)
        
        ephFile.close()
        
        #Counter
        i = i + 1

    #Plotting
    times = []
    xs = []
    ys = []
    zs = []
    rhos = []
    thetas = []
    phis = []
    
    for line in actualData:
        times.append(copy.copy(line[6]))
        x = copy.copy(line[0])
        y = copy.copy(line[1])
        z = copy.copy(line[2])
        
        rho = math.sqrt(x**2 + y**2 + z**2)
        theta = math.atan(y/x)
        phi = math.atan(math.sqrt(x**2 + y**2)/z)
        
        xs.append(x)
        ys.append(y)
        zs.append(z)
        
        rhos.append(rho)
        thetas.append(theta)
        phis.append(phi)
    
    outputFile = open('Masters/Actual_Master.csv','w')
    outputFileSpherical = open('Masters/Actual_Master_Spherical.csv','w')

    for i in range(len(times)):
        elapsedTime = float(times[i]) - 2458627.62899178240741
        outputFile.write(str(elapsedTime) + ',')
        outputFile.write(str(xs[i]) + ',')
        outputFile.write(str(ys[i]) + ',')
        outputFile.write(str(zs[i]) + '\n')
        
        outputFileSpherical.write(str(elapsedTime) + ',')
        outputFileSpherical.write(str(rhos[i]) + ',')
        outputFileSpherical.write(str(thetas[i]) + ',')
        outputFileSpherical.write(str(phis[i]) + '\n')

    outputFile.close()
    outputFileSpherical.close()

    rk4Times = []
    rk4Xs = []
    rk4Ys = []
    rk4Zs = []
    rk4Rhos = []
    rk4Thetas = []
    rk4Phis = []
    
    for line in rk4Data:
        rk4Times.append(copy.copy(line[6]))
        x = copy.copy(line[0])
        y = copy.copy(line[1])
        z = copy.copy(line[2])
        
        rho = math.sqrt(x**2 + y**2 + z**2)
        theta = math.atan(y/x)
        phi = math.atan(math.sqrt(x**2 + y**2)/z)
        
        rk4Xs.append(x)
        rk4Ys.append(y)
        rk4Zs.append(z)
        
        rk4Rhos.append(rho)
        rk4Thetas.append(theta)
        rk4Phis.append(phi)
        
    outputFile2 = open('Masters/RK4_Master.csv','w')
    outputFileSpherical2 = open('Masters/RK4_Master_Spherical.csv','w')

    for i in range(len(rk4Times)):
        elapsedTime = float(rk4Times[i]) - 2458627.62899178240741
        outputFile2.write(str(elapsedTime) + ',')
        outputFile2.write(str(rk4Xs[i]) + ',')
        outputFile2.write(str(rk4Ys[i]) + ',')
        outputFile2.write(str(rk4Zs[i]) + '\n')
        
        outputFileSpherical2.write(str(elapsedTime) + ',')
        outputFileSpherical2.write(str(rk4Rhos[i]) + ',')
        outputFileSpherical2.write(str(rk4Thetas[i]) + ',')
        outputFileSpherical2.write(str(rk4Phis[i]) + '\n')

    outputFile2.close()
    outputFileSpherical2.close()
