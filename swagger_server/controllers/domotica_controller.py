import connexion
from swagger_server.models.domotica import Domotica
from swagger_server.models.domotica_object import DomoticaObject
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def domotica_domoticaid_get():
    """
    domotica_domoticaid_get
    Gets the specific information from one Domotica object.  

    :rtype: DomoticaObject
    """
    return 'do some magic!'


def domotica_domoticaid_post(domoticaid):
    """
    domotica_domoticaid_post
    Activates a specific domotica object  
    :param domoticaid: Numeric ID of the Domotica to activate
    :type domoticaid: int

    :rtype: None
    """
    return 'do some magic!'


def domotica_get():
    """
    domotica_get
    Gets &#x60;Domotica&#x60; objects of the household. Corresponds to the objects that can be interacted with from the outside. 

    :rtype: List[Domotica]
    """
    return 'do some magic!'
