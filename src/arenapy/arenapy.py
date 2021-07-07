import requests
import json


# Access
def login(email, password, workspaceId):
    """Login to Arena BOM
    
    :param email: email associated with Arena BOM account
    :param password: password associated with Arena BOM account
    :param workspaceId: (optional) the id of the workspace being accessed
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = "https://api.arenasolutions.com/v1/login"

    payload = json.dumps({
        "email": email,
        "password": password,
        "workspaceId": workspaceId
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response

def logout(sessionId):
    """Logout of Arena BOM
    
    :param email: email associated with Arena BOM account
    :param password: password associated with Arena BOM account
    :param workspaceId: (optional) the id of the accessed workspace
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = "https://api.arenasolutions.com/v1/logout"

    payload = ""
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response

# Settings
## Item Settings
def itemSpecsAttributesGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/attributes?includePossibleValues=true"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemCategoriesGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/categories"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemCategoryGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/categories/FXH0EBFHS9S2L4K2MQPI"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemCategoryAttrubutesGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/categories/FXH0EBFHS9S2L4K2MQPI/attributes?includePossibleValues=true"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemBOMAttributesGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/bom/attributes?includePossibleValues=true"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemNumberFormatsGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/numberformats"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemNumberFormatGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/numberformats/R9TCQNRT4L4DWFXZDPKF"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemLifecyclePhasesGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/lifecyclephases"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemComplianceRequirementsGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/requirements"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def itemComplianceRequirementGet(sessionId):
    url = "https://api.arenasolutions.com/v1/settings/items/requirements/ASCV96ACN4LM5O71TLSH"

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

## Supplier Settings
# def supplierSummaryAttributesGet(sessionId):
