import requests
import json


base_url = "https://api.arenasolutions.com/v1"


# Access
def login(email, password, workspaceId):
    """Begin API session
    
    :param email: email associated with Arena BOM account
    :param password: password associated with Arena BOM account
    :param workspaceId: (optional) the id of the workspace being accessed
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/login"

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
    """Close API session
    
    :param sessionId: token for current user session
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/logout"

    payload = ""
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


# Item
def getItemSearch(sessionId, number):
    """Search for items in Arena by number
    
    :param sessionId: token for current user session
    :param number: item number to search by
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items?number={number}&limit=400".format(number=number)

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def getItemSpecs(sessionId, guid):
    """Get specs of a certain item
    
    :param sessionId: token for current user session
    :param guid: unique id of an item
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items/{guid}?includeEmptyAdditionalAttributes=true".format(guid=guid)

    payload={}
    headers = {
        'arena_session_id': sessionId,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


# Item BOM
def getItemBom(sessionId, guid):
    """Search for items in Arena by number
    
    :param sessionId: token for current user session
    :param guid: unique id of an item
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items/{guid}/bom".format(guid=guid)

    payload={}
    headers = {
    'arena_session_id': sessionId,
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response