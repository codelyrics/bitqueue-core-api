import connexion
import six

from openapi_server.models.org import Org  # noqa: E501
from openapi_server.models.tenant import Tenant  # noqa: E501
from openapi_server import util


def create_org(orgname):  # noqa: E501
    """create_org

    Create Organization # noqa: E501

    :param orgname: Organization name
    :type orgname: str

    :rtype: None
    """
    return 'do some magic!'


def create_tenant(orgid, tenantname):  # noqa: E501
    """create_tenant

    Create tenant # noqa: E501

    :param orgid: Organization ID
    :type orgid: int
    :param tenantname: Tenant name
    :type tenantname: str

    :rtype: None
    """
    return 'do some magic!'


def delete_org(orgid):  # noqa: E501
    """delete_org

    Delete Organization # noqa: E501

    :param orgid: Organization ID
    :type orgid: int

    :rtype: None
    """
    return 'do some magic!'


def delete_tenant(orgid, tenantid):  # noqa: E501
    """delete_tenant

    delete tenant # noqa: E501

    :param orgid: Organization ID
    :type orgid: int
    :param tenantid: Tenant Id
    :type tenantid: int

    :rtype: None
    """
    return 'do some magic!'


def get_org(orgname):  # noqa: E501
    """get_org

    Return Organization Details. # noqa: E501

    :param orgname: Organization name
    :type orgname: str

    :rtype: Org
    """
    return 'do some magic!'


def get_tenant_by_id(orgid, tenantid):  # noqa: E501
    """get_tenant_by_id

    Get tenants details # noqa: E501

    :param orgid: Organization ID
    :type orgid: int
    :param tenantid: Tenant Id
    :type tenantid: int

    :rtype: Tenant
    """
    return 'do some magic!'


def get_tenant_list(orgid):  # noqa: E501
    """get_tenant_list

    Get tenants details # noqa: E501

    :param orgid: Organization ID
    :type orgid: int

    :rtype: List[Tenant]
    """
    return 'do some magic!'
