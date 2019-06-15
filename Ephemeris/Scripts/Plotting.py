import matplotlib.pyplot as plt
import numpy as np

#%%Cartesian
actualFile = open('Masters/Actual_Master.csv','r')
rk4File = open('Masters/RK4_Master.csv','r')

actualLines = actualFile.readlines()
rk4Lines = rk4File.readlines()

actualTime = []
actualX = []
actualY = []
actualZ = []

rk4Time = []
rk4X = []
rk4Y = []
rk4Z = []

for i in range(len(actualLines)):
    actualLine = actualLines[i].split(',')
    rk4Line = rk4Lines[i].split(',')

    actualTime.append(float(actualLine[0]))
    actualX.append(float(actualLine[1]))
    actualY.append(float(actualLine[2]))
    actualZ.append(float(actualLine[3]))

    rk4Time.append(float(rk4Line[0]))
    rk4X.append(float(rk4Line[1]))
    rk4Y.append(float(rk4Line[2]))
    rk4Z.append(float(rk4Line[3]))

errorFile = open('Masters/Error_Cartesian.csv','r')
errorLines = errorFile.readlines()

errorTimes = []
Xerr = []
Yerr = []
Zerr = []
delta = []

for i in range(len(errorLines)):
    line = errorLines[i]
    line = line.split(',')
    errorTimes.append(float(line[0]))
    Xerr.append(float(line[1]))
    Yerr.append(float(line[2]))
    Zerr.append(float(line[3]))
    delta.append(float(line[4]))

actualFile.close()
rk4File.close()
errorFile.close()

#%%Spherical

actualFile = open('Masters/Actual_Master_Spherical.csv','r')
rk4File = open('Masters/RK4_Master_Spherical.csv','r')

actualLines = actualFile.readlines()
rk4Lines = rk4File.readlines()

actualTime = []
actualRho = []
actualTheta = []
actualPhi = []

rk4Time = []
rk4Rho = []
rk4Theta = []
rk4Phi = []

for i in range(len(actualLines)):
    actualLine = actualLines[i].split(',')
    rk4Line = rk4Lines[i].split(',')

    actualTime.append(float(actualLine[0]))
    actualRho.append(float(actualLine[1]))
    actualTheta.append(float(actualLine[2]))
    actualPhi.append(float(actualLine[3]))

    rk4Time.append(float(rk4Line[0]))
    rk4Rho.append(float(rk4Line[1]))
    rk4Theta.append(float(rk4Line[2]))
    rk4Phi.append(float(rk4Line[3]))


errorFile = open('Masters/Error_Spherical.csv','r')
errorLines = errorFile.readlines()

errorTimes2 = []
rhoErr = []
thetaErr = []
phiErr = []
gcDist = []

for i in range(len(errorLines)):
    line = errorLines[i]
    line = line.split(',')
    errorTimes2.append(float(line[0]))
    rhoErr.append(float(line[1]))
    thetaErr.append(float(line[2]))
    phiErr.append(float(line[3]))
    gcDist.append(float(line[4]))

actualFile.close()
rk4File.close()
errorFile.close()



#%%Plotting

actualTime
actualX
actualY
actualZ
rk4Time
rk4X
rk4Y
rk4Z
errorTimes
Xerr
Yerr
Zerr
delta
actualTime
actualRho
actualTheta
actualPhi
rk4Time
rk4Rho
rk4Theta
rk4Phi
errorTimes2
rhoErr
thetaErr
phiErr
gcDist
#Create figure
fig = plt.figure()
fig.suptitle('RK4 vs Actual Comparison')
fig.subplots_adjust(hspace=0.5)

ax = fig.add_subplot(321) #Cartesion coordinates
ax2 = fig.add_subplot(323) #Cartesian error
ax3 = fig.add_subplot(325) #Separation
ax4 = fig.add_subplot(322) #Spherical coordinates
ax5 = fig.add_subplot(324) #Spherical error
ax6 = fig.add_subplot(326) #FOV separation

#Set Limits
maxX = max(actualTime)

ax.set_xlim([0,maxX])
ax2.set_xlim([0,maxX])
ax3.set_xlim([0,maxX])
ax4.set_xlim([0,maxX])
ax5.set_xlim([0,maxX])
ax6.set_xlim([0,maxX])

#subplot titles
ax.title.set_text('Cartesian Coordinates')
ax2.title.set_text('Cartesian Error')
ax3.title.set_text('Separation')
ax4.title.set_text('Spherical Coordinates')
ax5.title.set_text('Spherical Error')
ax6.title.set_text('FOV Great-Circle Separation')

#subplot scales
ax2.set_yscale('log')
ax3.set_yscale('log')
ax5.set_yscale('log')
ax6.set_yscale('log')

#subplot axis labels
ax.set(xlabel='Time (days)',ylabel='Position (m)')
ax2.set(xlabel='Time (days)',ylabel='Percent Error')
ax3.set(xlabel='Time (days)',ylabel='Distance (m)')
ax4.set(xlabel='Time (days)',ylabel='Position (Radians)')
ax5.set(xlabel='Time (days)',ylabel='Percent Error')
ax6.set(xlabel='Time (days)',ylabel='Distance (m)')

#ax plot
ax.plot(actualTime,actualX,'.-',color='r',label='Actual X')
ax.plot(actualTime,actualY,'.-',color='g',label='Actual Y')
ax.plot(actualTime,actualZ,'.-',color='b',label='Actual Z')

ax.plot(rk4Time,rk4X,'.--',color='r',label='RK4 X')
ax.plot(rk4Time,rk4Y,'.--',color='g',label='RK4 Y')
ax.plot(rk4Time,rk4Z,'.--',color='b',label='RK4 Z')

#ax2 plot
ax2.plot(errorTimes,Xerr,'.-',color='r',label='X Error')
ax2.plot(errorTimes,Yerr,'.-',color='g',label='Y Error')
ax2.plot(errorTimes,Zerr,'.-',color='b',label='Z Error')

#ax3 plot
ax3.plot(errorTimes,delta,'.-',color='k',label='Separation')

#ax4 plot
ax4.plot(actualTime,actualTheta,'.-',color='g',label=r'Actual $\theta$')
ax4.plot(actualTime,actualPhi,'.-',color='b',label=r'Actual $\phi$')

ax4.plot(actualTime,rk4Theta,'.--',color='g',label=r'RK4 $\theta$')
ax4.plot(actualTime,rk4Phi,'.--',color='b',label=r'RK4 $\phi$')

#ax5 plot
ax5.plot(errorTimes2,rhoErr,'.-',color='r',label=r'$\rho$ Error')
ax5.plot(errorTimes2,thetaErr,'.-',color='g',label=r'$\theta$ Error')
ax5.plot(errorTimes2,phiErr,'.-',color='b',label=r'$\phi$ Error')

#ax6 plot
ax6.plot(errorTimes2,gcDist,'.-',color='k',label='Separation')

#Add legends
ax.legend(loc='upper left')
ax2.legend(loc='upper left')
ax3.legend(loc='upper left')
ax4.legend(loc='upper left')
ax5.legend(loc='upper left')
ax6.legend(loc='upper left')

plt.show()
