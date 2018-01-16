import connexion
from swagger_server.models.parameters import Parameters
from swagger_server.models.parameters1 import Parameters1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import pymysql


def query_execute_post(Parameters):
    """
    query_execute_post
    Executes the query  
    :param Parameters: Array of Parameters of the query.
    :type Parameters: list | bytes

    :rtype: None
    """
    query = "";

    connection = pymysql.connect(host='localhost', port=4000, user='root', passwd='', db='mysql')

    cursor = connection.cursor()


    print(cursor.description)

    for key, value in Parameters.items():
        if(key == "value"):
            query = value

    cursor.execute(query)


    for row in cursor:
        print(row)

    if connexion.request.is_json:
        Parameters = [Parameters1.from_dict(d) for d in connexion.request.get_json()]

    cursor.close()
    connection.close()

    return 'do some magic!'


def query_get():
    """
    query_get
    Returns the needed parameters for running a MySQL query in the current location 

    :rtype: List[Parameters]
    """
    return 'do some magic!'


# port 4000 for MySQL stukje schrijven met input query Connectieopenen, query uitvoeren op connectie alles wat daar uit komt returnen
