# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.domotica import Domotica
from swagger_server.models.domotica_object import DomoticaObject
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDomoticaController(BaseTestCase):
    """ DomoticaController integration test stubs """

    def test_domotica_domoticaid_get(self):
        """
        Test case for domotica_domoticaid_get

        
        """
        response = self.client.open('/domotica/{domoticaid}'.format(domoticaid=56),
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_domotica_domoticaid_post(self):
        """
        Test case for domotica_domoticaid_post

        
        """
        query_string = [('state', 56)]
        response = self.client.open('/domotica/{domoticaid}'.format(domoticaid=56),
                                    method='POST',
                                    query_string=query_string)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_domotica_get(self):
        """
        Test case for domotica_get

        
        """
        response = self.client.open('/domotica',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
