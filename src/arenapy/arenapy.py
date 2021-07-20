import requests
from requests.models import Response
import json
import copy


base_url = "https://api.arenasolutions.com/v1"


# Utils
def __build_response(status_code, content):
    response = Response()
    response.status_code = status_code
    response.content = b'{}'.format(content)

    return response

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
def getItemSearch(session_id, searchable_attributes):
    """Search for items in given parameters/values
    
    :param session_id: token for current user session
    :param searchable_attributes: dict of attribute/value key pairs to search by
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    # Get attributes
    result = getItemSpecsAttributes(session_id)
    try:
        attributes = json.loads(result.content)['results']
    except KeyError as e:
        return __build_response(status_code=400, content={'error': 'KeyError: {}'.format(e)})

    # Check params for attributes
    searchable_attributes_copy = copy.deepcopy(searchable_attributes)
    for attribute in searchable_attributes.keys():
        try:
            result = next((dict for dict in attributes if dict['name'] == attribute), None)
        except KeyError:
            continue
        if (result == None):
            continue
        else:
            searchable_attributes_copy[result['guid']] = searchable_attributes[attribute]
            del searchable_attributes_copy[attribute]
        

    url = base_url + '/items?'
    for key, value in searchable_attributes_copy.items():
        url = url + '{param}={value}&'.format(param=key, value=value)

    url = url[:-1]

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


# Settings
## Item Settings
def getItemSpecsAttributes(sessionId):
    url = base_url + "/settings/items/attributes?includePossibleValues=true"

    payload={}
    headers = {
        'arena_session_id': sessionId,
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


# File
def getFileContent(session_id, guid):
    """Get the contents of a file
    
    :param session_id: token for current user session
    :param guid: unique id of an item
    :return: :class:'Response <Response>' object
    :rtype: requests.Response
    """

    url = base_url + "/files/{guid}/content".format(guid=guid)

    payload={}
    headers = {
        'arena_session_id': session_id,
        'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return response