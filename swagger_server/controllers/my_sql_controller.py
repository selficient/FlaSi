import connexion
from swagger_server.models.parameters import Parameters
from swagger_server.models.parameters1 import Parameters1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def query_execute_post(Parameters):
    """
    query_execute_post
    Executes the query  
    :param Parameters: Array of Parameters of the query.
    :type Parameters: list | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Parameters = [Parameters1.from_dict(d) for d in connexion.request.get_json()]
    return 'do some magic!'


def query_get():
    """
    query_get
    Returns the needed parameters for running a MySQL query in the current location 

    :rtype: List[Parameters]
    """
    return 'do some magic!'
