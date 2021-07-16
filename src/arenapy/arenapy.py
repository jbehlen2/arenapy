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

def logout(session_id):
    """Close API session
    
    :param session_id: token for current user session
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/logout"

    payload = ""
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    return response


# Item
def getItemSearchByNumber(session_id, number):
    """Search for items in Arena by number
    
    :param session_id: token for current user session
    :param number: item number to search by
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items?number={number}&limit=400".format(number=number)

    payload={}
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def getItemSearchByFinishedGood(session_id, param):
    """Search for items in Arena by finished good attribute
    
    :param session_id: token for current user session
    :param param: yes or no
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items?SAUDI7DIJBSATCRUN66M={param}&limit=400".format(param=param)

    payload={}
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response

def getItemSpecs(session_id, guid):
    """Get specs of a certain item
    
    :param session_id: token for current user session
    :param guid: unique id of an item
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items/{guid}?includeEmptyAdditionalAttributes=true".format(guid=guid)

    payload={}
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


# Item BOM
def getItemBom(session_id, guid):
    """Get the BOM of an item
    
    :param session_id: token for current user session
    :param guid: unique id of an item
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items/{guid}/bom".format(guid=guid)

    payload={}
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response


# Item Files
def getItemFiles(session_id, guid):
    """Get files from an item
    
    :param session_id: token for current user session
    :param guid: unique id of an item
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/items/{guid}/files".format(guid=guid)

    payload={}
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response