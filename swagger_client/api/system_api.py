# coding: utf-8

"""
    Insights.Api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SystemApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def system_demand_control_instructions_get(self, **kwargs):  # noqa: E501
        """Demand control instructions (DCI)  # noqa: E501

        This endpoint provides demand control instruction data, filtered by the time range of the instruction.  There is no date range limit on parameters.  If no query parameters are supplied all data is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_demand_control_instructions_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from:
        :param datetime to:
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.system_demand_control_instructions_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.system_demand_control_instructions_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def system_demand_control_instructions_get_with_http_info(self, **kwargs):  # noqa: E501
        """Demand control instructions (DCI)  # noqa: E501

        This endpoint provides demand control instruction data, filtered by the time range of the instruction.  There is no date range limit on parameters.  If no query parameters are supplied all data is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_demand_control_instructions_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from:
        :param datetime to:
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'to', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method system_demand_control_instructions_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/system/demand-control-instructions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscDemandControlInstructionData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def system_frequency_get(self, **kwargs):  # noqa: E501
        """System frequency (FREQ)  # noqa: E501

        This endpoint allows for retrieving a collection of recent system frequency data from National Grid ESO. Results  can be filtered by a range of DateTime parameters. This endpoint is useful for ad-hoc querying frequency data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_frequency_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from:
        :param datetime to:
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.system_frequency_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.system_frequency_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def system_frequency_get_with_http_info(self, **kwargs):  # noqa: E501
        """System frequency (FREQ)  # noqa: E501

        This endpoint allows for retrieving a collection of recent system frequency data from National Grid ESO. Results  can be filtered by a range of DateTime parameters. This endpoint is useful for ad-hoc querying frequency data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_frequency_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from:
        :param datetime to:
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'to', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method system_frequency_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/system/frequency', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemFrequency',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def system_frequency_stream_get(self, **kwargs):  # noqa: E501
        """System frequency (FREQ) stream  # noqa: E501

        This endpoint allows for retrieving a stream of recent system frequency data from National Grid ESO. Results can  be filtered by a range of DateTime parameters. This endpoint has an optimised JSON payload and aimed at frequent  request for the frequency data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_frequency_stream_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from:
        :param datetime to:
        :return: list[InsightsApiModelsResponsesMiscSystemFrequency]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.system_frequency_stream_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.system_frequency_stream_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def system_frequency_stream_get_with_http_info(self, **kwargs):  # noqa: E501
        """System frequency (FREQ) stream  # noqa: E501

        This endpoint allows for retrieving a stream of recent system frequency data from National Grid ESO. Results can  be filtered by a range of DateTime parameters. This endpoint has an optimised JSON payload and aimed at frequent  request for the frequency data.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_frequency_stream_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime _from:
        :param datetime to:
        :return: list[InsightsApiModelsResponsesMiscSystemFrequency]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_from', 'to']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method system_frequency_stream_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/system/frequency/stream', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InsightsApiModelsResponsesMiscSystemFrequency]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def system_warnings_get(self, **kwargs):  # noqa: E501
        """System warnings (SYSWARN)  # noqa: E501

        This endpoint provides system warnings data. Results can be filtered by warning type and a range of DateTime parameters.  - If no parameters are specified then the latest message is returned  - If just a warning type is specified then the latest message of that type is returned  - If just publish times are specified then all messages within that range are returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_warnings_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str warning_type:
        :param datetime publish_date_time_from:
        :param datetime publish_date_time_to:
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.system_warnings_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.system_warnings_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def system_warnings_get_with_http_info(self, **kwargs):  # noqa: E501
        """System warnings (SYSWARN)  # noqa: E501

        This endpoint provides system warnings data. Results can be filtered by warning type and a range of DateTime parameters.  - If no parameters are specified then the latest message is returned  - If just a warning type is specified then the latest message of that type is returned  - If just publish times are specified then all messages within that range are returned  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.system_warnings_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str warning_type:
        :param datetime publish_date_time_from:
        :param datetime publish_date_time_to:
        :param str format: Response data format. Use json/xml to include metadata.
        :return: InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['warning_type', 'publish_date_time_from', 'publish_date_time_to', 'format']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method system_warnings_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'warning_type' in params:
            query_params.append(('warningType', params['warning_type']))  # noqa: E501
        if 'publish_date_time_from' in params:
            query_params.append(('publishDateTimeFrom', params['publish_date_time_from']))  # noqa: E501
        if 'publish_date_time_to' in params:
            query_params.append(('publishDateTimeTo', params['publish_date_time_to']))  # noqa: E501
        if 'format' in params:
            query_params.append(('format', params['format']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json', 'application/xml', 'text/xml', 'text/csv'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/system/warnings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InsightsApiModelsResponsesResponseWithMetadata1InsightsApiModelsResponsesMiscSystemWarningsData',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
