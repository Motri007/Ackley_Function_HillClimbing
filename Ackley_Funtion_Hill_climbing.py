import math
import random

rand = random.Random()

@staticmethod
def Ackley(x, y):
    a = -20 * math.exp(-0.2 * math.sqrt(0.5 * (x * x + y * y)))
    b = -math.exp(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
    return a + b + math.e + 20

@staticmethod
def main():
    x = rand.random() - 0.5
    y = rand.random() - 0.5 
    behtarin = Ackley(x, y) 

    tedadbarresi = 0 

    while tedadbarresi < 100:
        sizestep = rand.random()
        newx = x * sizestep
        newy = y * sizestep
        

        newvalue = Ackley(newx, newy)

        if newvalue < behtarin:
            x = newx
            y = newy
            behtarin = newvalue

        tedadbarresi += 1

    Xjadid = int(x)
    Yjadid = int(y)
    BestValueInt = int(behtarin)

    print(f"Noghte pain Ackley Function: ({Xjadid},{Yjadid})")  
    print(f"Behtarin Value az Ackley:{behtarin} ≈ {BestValueInt}")
    print(f"Tedad barresi noghat hamsaye: {tedadbarresi}")

main()