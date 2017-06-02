#!/usr/bin/env python3

# Description : Programme permettant de générer un fichier SVG
#               contenant un graphique à partir d'un fichier historique
#               stockant les données du serveur snmp
# Auteurs : Lucas Bulloni, Malik Fleury et Bastien Wermeille
# Data : 02.06.2017
# Version : 1.0

import matplotlib.pyplot as plt
import numpy as np

# Lecture des données
def ReadFile(filePath):
    time = []
    octets = []
    #Récupération des données
    with open(filePath, "r") as f:
        for line in f.readlines():
            if line != "\n" :
                t, o = line.split(" ")
                time.append(t)
                octets.append(o)
        f.close()
        return (time,octets)
    return (None,None)

# Generation du graphique
def GenerateFile(data):
    plt.plot(data[0], data[1])
    plt.ylabel('bytes (o)')
    plt.xlabel('time (s)')
    plt.title('Bytes at time')
    plt.grid(True)
    plt.savefig("graph.svg",type="svg")
    #plt.show()

# Main programme
GenerateFile(ReadFile("historique"))
