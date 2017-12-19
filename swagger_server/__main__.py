#!/usr/bin/env python3

import connexion
from .encoder import JSONEncoder


if __name__ == '__main__':
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'The FlaSi webservice connects the HomeLynk system to the outside world. It is the main entry point into the Selficient house. It gives the user the possibility to read the MySQL database that is connected to the house, as well as send signals to the local domotica objects'})
    app.run(port=8080)
