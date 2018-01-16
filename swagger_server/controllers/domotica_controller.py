import connexion
from swagger_server.models.domotica import Domotica
from swagger_server.models.domotica_object import DomoticaObject
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
from flask import Response

def domotica_domoticaid_get():
    """
    domotica_domoticaid_get
    Gets the specific information from one Domotica object.  

    :rtype: DomoticaObject
    """

    domoticafile = open("domotica-items.txt", "r")
    print(domoticafile)


    return domoticafile.readline()  


def domotica_domoticaid_post(domoticaid):
    """
    domotica_domoticaid_post
    Activates a specific domotica object  
    :param domoticaid: Numeric ID of the Domotica to activate
    :type domoticaid: int

    :rtype: None
    """
    with open("domotica-items.txt", "r") as domoticafile:
        inputstring = domoticafile.readline().replace("\n","")
        for line in domoticafile:
                items = line.replace(" ", "").split("|")
                print(items[0])
                if items[0] == str(domoticaid):
                    return createObject(inputstring,line)

    return customerror("Geen item gevonden met dit ID", 501)

def domotica_get():
    """
    domotica_get
    Gets &#x60;Domotica&#x60; objects of the household. Corresponds to the objects that can be interacted with from the outside. 

    :rtype: List[Domotica]
    """

    with open("domotica-items.txt", "r") as domoticafile:
        return domoticafile.read()

def customerror(errormessage, code):
    return Response('{"error":"' + errormessage + '"}', status=code, mimetype='application/json')

def createObject(inputstring, outputstr):
    objectcomponents = outputstr.replace(" ", "").split("|")
    objectkeys = inputstring.replace(" ", "").split("|")
    newdictionary = {}
    counter = 0
    for key in objectkeys:
        newdictionary[key] = objectcomponents[counter]
        counter += 1

    return newdictionary
