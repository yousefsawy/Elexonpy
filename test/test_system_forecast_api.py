# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.system_forecast_api import SystemForecastApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSystemForecastApi(unittest.TestCase):
    """SystemForecastApi unit test stubs"""

    def setUp(self):
        self.api = SystemForecastApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_forecast_system_loss_of_load_get(self):
        """Test case for forecast_system_loss_of_load_get

        Loss of load probability and de-rated margin forecast (LOLPDRM)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
