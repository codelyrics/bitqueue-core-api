# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.org import Org  # noqa: E501
from openapi_server.models.tenant import Tenant  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_org_get(self):
        """Test case for org_get

        
        """
        query_string = [('orgname', 'orgname_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/bitqueue/api/org',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_org_orgid_tenant_get(self):
        """Test case for org_orgid_tenant_get

        
        """
        headers = { 
            'Accept': 'aplication/json',
        }
        response = self.client.open(
            '/bitqueue/api/org/{orgid}/tenant'.format(orgid=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_org_orgid_tenant_post(self):
        """Test case for org_orgid_tenant_post

        
        """
        tenant = {}
        query_string = [('tenantname', 'tenantname_example')]
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/bitqueue/api/org/{orgid}/tenant'.format(orgid=1),
            method='POST',
            headers=headers,
            data=json.dumps(tenant),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_org_orgid_tenant_tenantid_get(self):
        """Test case for org_orgid_tenant_tenantid_get

        
        """
        headers = { 
            'Accept': 'aplication/json',
        }
        response = self.client.open(
            '/bitqueue/api/org/{orgid}/tenant/{tenantid}'.format(orgid=1, tenantid=1),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_org_post(self):
        """Test case for org_post

        
        """
        org = {}
        query_string = [('orgname', 'orgname_example')]
        headers = { 
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/bitqueue/api/org',
            method='POST',
            headers=headers,
            data=json.dumps(org),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
