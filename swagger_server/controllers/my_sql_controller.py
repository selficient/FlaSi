import connexion
from swagger_server.models.parameters import Parameters
from swagger_server.models.parameters1 import Parameters1
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime

import config
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

    query = ""

    # config.py holds all information that is needed to initialise the MySQL database
    connection = pymysql.connect(host=config.databaseIP, port=config.databasePort, user=config.databaseUsername,
                                 passwd=config.databasePassword, db=config.databaseDatabasename)

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

    columnames = [i[0] for i in cursor.description]

    for row in cursor:
        queryresult.append(row)

    if connexion.request.is_json:
        Parameters = [Parameters1.from_dict(d) for d in connexion.request.get_json()]

    cursor.close()
    connection.close()

    try:
        objectlist = createObject(columnames, queryresult)
    except:
        return customerror("Er konden geen objecten aangemaakt worden voor de gegeven dataset", 500)

    return objectlist



def query_get():
    """
    query_get
    Returns the needed parameters for running a MySQL query in the current location

    :rtype: List[Parameters]
    """

    exampleParameters = {
        "name": "Naam van de parameter, bijvoorbeeld: query",
        "type": "Type van de parameter, bijvoorbeeld: mysql-query",
        "value": "Daadwerkelijke waarde van de parameter, bijvoorbeeld een select statement",
        "example": "Voorbeeld van de parameter wanneer nodig, kan vaak leeg blijven"
    }

    return [exampleParameters]

def customerror(errormessage, code):
    # returns customised error after methods get initialised
    return Response('{"error":"' + errormessage + '"}', status=code, mimetype='application/json')

def createObject(columnames, data):
    # creates an object based on the columndates and data
    # returns object that can be requested on Postman
    emptyList = []
    lengthOfColumns = len(columnames)
    if(lengthOfColumns != 0):
        for row in data:
            object = {}
            counter = 0
            for column in columnames:
                object[column] = row[counter]
                counter += 1
                if counter > lengthOfColumns:
                    break

            emptyList.append(object)

    return emptyList
