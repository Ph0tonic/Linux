#!/usr/bin/env python3
#!/usr/bin/env python

# Description : Serveur snmp qui permet d'effectuer des requetes SNMP
#               sur un equipement reseau et qui va enregistrer
#               les donnees dans un fichier "historique"
# Auteurs : Lucas Bulloni, Malik Fleury et Bastien Wermeille
# Date : 02.06.2017
# Version : 1.0

#SOURCE CODE FROM https://makina-corpus.com/blog/metier/2016/initiation-a-snmp-avec-python-pysnmp-partie2
#                 http://pysnmp.sourceforge.net/docs/hlapi/asyncore/sync/manager/cmdgen/getcmd.html

from threading import Timer
from time import time
from pysnmp.hlapi import *
from pysnmp.smi.view import MibViewController

class SnmpTool:
    def __init__(self,ip,port, log_filename):
        self.ip = ip
        self.port = port
        self.log_filename = log_filename
        self.engine = SnmpEngine()                              # Coeur de pySNMP
        self.community = CommunityData('public', mpModel=0)     # Communaute
        self.transport = UdpTransportTarget((ip,port))          # Protocole couche 4 : UDP
        self.logfile = open(log_filename, 'a')

    def read(self, object_type_id):
        # Generation de la commande et envoi
        err_indic, err_stat, err_index, var_binds = next(getCmd(self.engine, self.community,
                                                                self.transport, ContextData(),
                                                                object_type_id))

        # Gestion des erreurs et affichage du resultat si OK
        if err_indic:
            print(err_indic)
        else:
            if err_stat:
                print('bug')
            else:
                # Ajout des donnees dans le fichier
                for name, val in var_binds:
                    print ("Lecture des octets de l'interface reussie")
                    self.logfile.write(str(int(time())) + ' %s\n' % ( val.prettyPrint()))


snmpt = SnmpTool('157.26.77.13', 161, "historique")
ot = ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.1'))
snmpt.read(ot)
