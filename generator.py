#!/usr/bin/env python3

# Description : Programme permettant de generer un fichier SVG
#               contenant un graphique a partir d'un fichier historique
#               stockant les donnees du serveur snmp
# Auteurs : Lucas Bulloni, Malik Fleury et Bastien Wermeille
# Date : 02.06.2017
# Version : 1.0

import matplotlib.pyplot as plt
import numpy as np
import datetime

# Lecture des donnees
def ReadFile(filePath):
    time = []
    octets = []
    firstLine = True
    date = ""
    TimeStamp = 0
    BaseOctets = 0
    #Recuperation des donnees
    with open(filePath, "r") as f:
        for line in f.readlines():
            if line != "\n" :
                t, o = line.split(" ")
                if firstLine == True:
                    firstLine = False
                    TimeStamp = int(t)
                    BaseOctets = int(o)
                    date = datetime.datetime.fromtimestamp(int(t)).strftime('%Y-%m-%d %H:%M:%S')
                time.append(int(t)-TimeStamp)
                octets.append(int(o)-BaseOctets)
        f.close()
        if len(time) <= 0:
            print("Error file empty")
            exit(-1)
        if len(time) != len(octets):
            print("Incorrect file")
            exit(-1)
        return (time,octets,date)
    print("Error while file loading")
    exit(-1)

# Generation du graphique
def GenerateFile(data):
    plt.plot(data[0], data[1])
    plt.ylabel('bytes (o)')
    plt.xlabel('time (s)')
    plt.title('Bytes from '+data[2])
    plt.grid(True)
    plt.savefig("graph.svg",type="svg")
    #plt.show()

# Main programme
GenerateFile(ReadFile("historique"))
print("Successful Generation !!!")
exit(1)
