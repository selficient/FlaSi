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
    if connexion.request.is_json:
        Parameters = [Parameters1.from_dict(d) for d in connexion.request.get_json()]

    query = "";

    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='BDSD')

    cursor = connection.cursor()

    for parameter in Parameters:
        if parameter.name == "query":
            query = parameter.value

    cursor.execute(query)

    queryresult = []

    for row in cursor:
        queryresult.append(row)

    if connexion.request.is_json:
        Parameters = [Parameters1.from_dict(d) for d in connexion.request.get_json()]

    cursor.close()
    connection.close()

    return queryresult


def query_get():
    """
    query_get
    Returns the needed parameters for running a MySQL query in the current location

    :rtype: List[Parameters]
    """
    return 'do some magic!'
