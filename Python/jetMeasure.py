import jetFunctions as j

directionPin = 27
enablePin = 22
points = 100
n = 10

try:
    measures = []
    j.initSpiAdc()
    j.initStepMotorGpio()
    for i in range(points):
        measures.append(j.getAdc())
        j.stepBackward(n)
finally:
    j.save(measures, n)
    j.stepForward(n * points)
    j.deinitSpiAdc()
    j.deinitStepMotorGpio()