# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Org(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, orgid=None, created=None, updated=None, uuid=None):  # noqa: E501
        """Org - a model defined in OpenAPI

        :param name: The name of this Org.  # noqa: E501
        :type name: str
        :param orgid: The orgid of this Org.  # noqa: E501
        :type orgid: int
        :param created: The created of this Org.  # noqa: E501
        :type created: str
        :param updated: The updated of this Org.  # noqa: E501
        :type updated: str
        :param uuid: The uuid of this Org.  # noqa: E501
        :type uuid: str
        """
        self.openapi_types = {
            'name': str,
            'orgid': int,
            'created': str,
            'updated': str,
            'uuid': str
        }

        self.attribute_map = {
            'name': 'name',
            'orgid': 'orgid',
            'created': 'created',
            'updated': 'updated',
            'uuid': 'uuid'
        }

        self._name = name
        self._orgid = orgid
        self._created = created
        self._updated = updated
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Org':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The org of this Org.  # noqa: E501
        :rtype: Org
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Org.


        :return: The name of this Org.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Org.


        :param name: The name of this Org.
        :type name: str
        """

        self._name = name

    @property
    def orgid(self):
        """Gets the orgid of this Org.


        :return: The orgid of this Org.
        :rtype: int
        """
        return self._orgid

    @orgid.setter
    def orgid(self, orgid):
        """Sets the orgid of this Org.


        :param orgid: The orgid of this Org.
        :type orgid: int
        """

        self._orgid = orgid

    @property
    def created(self):
        """Gets the created of this Org.


        :return: The created of this Org.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Org.


        :param created: The created of this Org.
        :type created: str
        """

        self._created = created

    @property
    def updated(self):
        """Gets the updated of this Org.


        :return: The updated of this Org.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this Org.


        :param updated: The updated of this Org.
        :type updated: str
        """

        self._updated = updated

    @property
    def uuid(self):
        """Gets the uuid of this Org.


        :return: The uuid of this Org.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Org.


        :param uuid: The uuid of this Org.
        :type uuid: str
        """

        self._uuid = uuid