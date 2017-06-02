#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def ReadFile(filePath):
    time = []
    octets = []
    #Récupération des données
    with open(filePath, "r") as f:
        for line in f.readlines():
            t, o = line.split(" ")
            time.append(t)
            octets.append(o)
        f.close()
        return (time,octets)
    return (None,None)


(time,octets) = ReadFile("historique")
#print(type(data))
#print(data)
print(time)
print(octets)

plt.plot(time, octets)

plt.xlabel('bytes (o)')
plt.ylabel('time (s)')
plt.title('Bytes at time')
plt.grid(True)
plt.savefig("graph.svg",type="svg")
plt.show()
