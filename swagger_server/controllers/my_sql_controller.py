import connexion
from swagger_server.models.parameters import Parameters
from swagger_server.models.parameters1 import Parameters1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import pymysql
from flask import Response

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
    try:
        cursor = connection.cursor()
    except:
        return customerror("Er kon geen verbinding worden gemaakt met de database", 500)

    if len(Parameters) == 0:
        return customerror("Er zijn geen parameters opgegeven", 500)

    for parameter in Parameters:
        if parameter.name == "query":
            query = parameter.value

    try:
        cursor.execute(query)
    except:
        return customerror("De Query kon niet uitgevoerd worden", 500)

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

def customerror(errormessage, code):
    return Response('{"error":"' + errormessage + '"}', status=code, mimetype='application/json')
