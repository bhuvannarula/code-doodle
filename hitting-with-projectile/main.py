from math import sin, cos, tan, atan, pi
from matplotlib import pyplot
import numpy

def Range(initialVelocity, angle, accnGrav = 9.8):
    tempRange = (initialVelocity**2) * sin(2*angle) / accnGrav
    return tempRange

def trajectory(startC, initialVelocity, pointtoHit, pointsAbove = [], pointsBelow = [], accnGrav = 9.8, precision = 2):
    '''
    function which returns the angle required to hit according to given data.

    startC is the point (x,y) where projectile starts
    initialVelocity is the initial velocity of projectile
    pointtoHit is point (x,y) where projectile is required to hit
    pointsAbove & pointsBelow are to be used in future
    accnGrav is acceleration due to gravity
    precision determines how near the trajectory will be to the 'hit point'
    '''
    startAngle = atan((pointtoHit[1] - startC[1])/(pointtoHit[0] - startC[0]))
    x = pointtoHit[0] - startC[0]
    initY = pointtoHit[1] - startC[1]
    count = 1
    def tryAngleValue(angle, dAngle, count):
        sign = (-1)**count
        angle += dAngle
        if angle >= (pi/2):
            print("Can't do that!")
            raise ValueError
        tempRange = Range(initialVelocity, angle, accnGrav)
        dy = x*tan(angle)*(1 - (x/tempRange)) - initY
        if round(abs(dy),precision) <= 1/(10**precision):
            return angle
        elif dy*sign > 0:
            return tryAngleValue(angle,dAngle, count)
        elif dy*sign < 0:
            count += 1
            return tryAngleValue(angle, -dAngle/2, count)
    return tryAngleValue(startAngle,pi/32, count)

'''
trajectory() function returns the angle required for projectile to hit at the given velocity.
'''
startC = (0,0) # the point where projectile will start
pointtoHit = (8,12) # the point where we need to reach

'''
Now, we can vary the initial velocity to create different trajectories.

Following code is for plotting graph for trajectories with initialVelocity in range(1,20)
'''

xHit, yHit = ((pointtoHit[i] - startC[i]) for i in range(2))
pyplot.plot(xHit,yHit, 'ro') # i don't know what 'ro' means, looked up on stackoverflow, this plots 'hit point'

for initialVelocity in range(1,20):
    try:
        angleFinal = trajectory(startC, initialVelocity, pointtoHit, precision=5)
    except ValueError:
        pass
    else:
        finalRange = Range(initialVelocity, angleFinal)
        def projectileEquation(x, angle = angleFinal, r = finalRange): # this is equation of projectile for graph
            return x*tan(angle)*(1-(x/r))
        x = numpy.arange(0,finalRange, 0.1)
        y = projectileEquation(x)
        pyplot.plot(x,y)

pyplot.show()