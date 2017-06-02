#!/usr/bin/env python3

from pysnmp.hlapi import *
from pysnmp.smi.view import MibViewController


#SOURCES : https://makina-corpus.com/blog/metier/2016/initiation-a-snmp-avec-python-pysnmp-partie2
#        : http://pysnmp.sourceforge.net/docs/hlapi/asyncore/sync/manager/cmdgen/getcmd.html
def snmp_read_counter_bytes():
    ip = '157.26.77.13'     # Ip de l'agent
    port = 161              # Port

    se = SnmpEngine()                        # Coeur de la bibliothèque pySNMP
    cd = CommunityData('public', mpModel=0)  # Paramètres d'auth : SNMPv1
    utt = UdpTransportTarget((ip, port))     # Protocole C4 : UDP
    ot1 = ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.1'))  # Identifiant info. : nombre d'octets sur interface 1
    ot2 = ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.10.2'))  # Identifiant info. : nombre d'octets sur interface 2

    # Generation de la commande et envoi
    errIndic, errStat, errIndexgcmd, varBinds = next(getCmd(se, cd, utt, ContextData(), ot1, ot2))

    # Gestion des erreurs et affichage du résultat si OK
    if errIndic:
        print(errIndic)
    else:
        if errStat:
            print('bug')
        else:
            # ajout des données dans le fichier
            for name, val in varBinds:
                print('%s = %s' % (name.prettyPrint(), val.prettyPrint()))

snmp_read_counter_bytes()
