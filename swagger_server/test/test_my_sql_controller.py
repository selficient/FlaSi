# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.domotica import Domotica
from swagger_server.models.parameters import Parameters
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestMySQLController(BaseTestCase):
    """ MySQLController integration test stubs """

    def test_query_execute_post(self):
        """
        Test case for query_execute_post

        
        """
        Parameters = [Parameters()]
        response = self.client.open('/query/execute',
                                    method='POST',
                                    data=json.dumps(Parameters),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_query_get(self):
        """
        Test case for query_get

        
        """
        response = self.client.open('/query',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
