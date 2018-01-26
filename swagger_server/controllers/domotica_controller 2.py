import connexion
from swagger_server.models.domotica import Domotica
from swagger_server.models.domotica_object import DomoticaObject
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import requests
from flask import Response
import config

def domotica_domoticaid_get(domoticaid):
    """
    domotica_domoticaid_get
    Gets the specific information from one Domotica object.
    :param domoticaid: Numeric ID of the Domotica to activate
    :type domoticaid: int

    :rtype: DomoticaObject
    """
    with open("domotica-items.txt", "r") as domoticafile:
        inputstring = domoticafile.readline().replace("\n","")
        for line in domoticafile:
                items = line.replace(" ", "").split("|")
                if items[0] == str(domoticaid):
                    return createObject(inputstring,line)

    return customerror("Geen item gevonden met dit ID", 501)


def domotica_domoticaid_post(domoticaid):
    """
    domotica_domoticaid_post
    Activates a specific domotica object
    :param domoticaid: Numeric ID of the Domotica to activate
    :type domoticaid: int

    :rtype: None
    """
    domoticafile = open("domotica-items.txt", "r")

    # Username and password for the HomeLynk are stored in cpnfig.py
    username = config.homeLynkUsername
    password = config.homeLynkPassword
    ipadresswebserver = config.homeLynkIP

    domoticaobject = domotica_domoticaid_get(domoticaid)
    groupadress = domoticaobject['GROUP']
    value = domoticaobject['VALUES']

    try:
        on = False
        try:
            statuslampjes = requests.get(ipadresswebserver+ '/leds')
            ledjes = statuslampjes.text.replace("\"", "").replace("{","").replace("}","").replace("\n","").replace(" ", "").split(":")


            if ledjes[-1] == "1,":
                on = True
            else:
                on = False
        except Exception as e:
            return customerror("Fout bij het ophalen van de huidige LED status", str(e), 500)


        if on:
            leds = '{ "Led1": 0, "Led2": 0, "Led3": 0}'
        else:
            leds = '{ "Led1": 1, "Led2": 1, "Led3": 1}'

        r = requests.put(ipadresswebserver + '/leds', data=leds)

    except Exception as e:
        return customerror("Fout bij het switchen van de status", str(e), 500)

    domoticafile.close()

    return succesfulloperation("Fantastisch!", 200)

def domotica_get():
    """
    domotica_get
    Gets &#x60;Domotica&#x60; objects of the household. Corresponds to the objects that can be interacted with from the outside.

    :rtype: List[Domotica]
    """
    with open("domotica-items.txt", "r") as domoticafile:
        return domoticafile.read()

def customerror(errormessage, exception, code):
    return Response(' {"error":"' + errormessage + '", "exception":"' + exception + '"}', status=code, mimetype='application/json')

def succesfulloperation(message, code):
    return Response('{"message":"' + message + '"}', status=code, mimetype='application/json')

def createObject(inputstring, outputstr):
    #create object based on the inputstring and refactores it to return a dictionary
    objectcomponents = outputstr.replace(" ", "").split("|")
    objectkeys = inputstring.replace(" ", "").split("|")
    objectDictionary = {}
    counter = 0
    for key in objectkeys:
        objectDictionary[key] = objectcomponents[counter]
        counter += 1
    return objectDictionary