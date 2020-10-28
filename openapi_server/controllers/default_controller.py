import connexion
import six

from openapi_server.models.org import Org  # noqa: E501
from openapi_server.models.tenant import Tenant  # noqa: E501
from openapi_server import util


def org_get(orgname):  # noqa: E501
    """org_get

    Return Organization Details. # noqa: E501

    :param orgname: Organization name
    :type orgname: str

    :rtype: Org
    """
    return 'do some magic!'


def org_orgid_tenant_get(orgid):  # noqa: E501
    """org_orgid_tenant_get

    Get tenants details # noqa: E501

    :param orgid: Organization ID
    :type orgid: int

    :rtype: List[Tenant]
    """
    return 'do some magic!'


def org_orgid_tenant_post(orgid, tenantname, tenant):  # noqa: E501
    """org_orgid_tenant_post

    Create tenant # noqa: E501

    :param orgid: Organization ID
    :type orgid: int
    :param tenantname: Tenant name
    :type tenantname: str
    :param tenant: Create Tenant
    :type tenant: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        tenant = Tenant.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def org_orgid_tenant_tenantid_get(orgid, tenantid):  # noqa: E501
    """org_orgid_tenant_tenantid_get

    Get tenants details # noqa: E501

    :param orgid: Organization ID
    :type orgid: int
    :param tenantid: Tenant Id
    :type tenantid: int

    :rtype: Tenant
    """
    return 'do some magic!'


def org_post(orgname, org):  # noqa: E501
    """org_post

    Create Organization # noqa: E501

    :param orgname: Organization name
    :type orgname: str
    :param org: Create org
    :type org: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        org = Org.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
