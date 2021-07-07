# Arenapy

Arenapy is a Python-implementation of the [Arena Solutions](https://www.arenasolutions.com/) API.

```
>>> from arenapy import arenapy
>>> sessionId = arenapy.login(email, password, workspaceId)

...

>>> arenapy.itemSearch(sessionId)
{  
   "count":20,
   "results":[  
      {  
         "category":{  
            "guid":"5N6P8RAK3MY6UNTA"
         },
         "creationDateTime":"2011-06-02T19:23:31Z",
         "guid":"VDXGLBCCLSBSBQMM0SJU",
         "lifecyclePhase":{  
            "guid":"7G6P3WAD3MG6GNFD",
            "name":"In Production"
         },
         "name":"PCBA, EveryRoad, Model 300",
         "number":"830-00001",
         "revisionNumber":"D"
      },
      ...
   ]
}

...

>>> response = arenapy.logout(sessionId)
```
---
## Installing Arenapy and Supported Versions
Arenapy is available on PyPi:
```
python -m pip install arenapy
```
Arenapy officially supports Python 3.6+.

---

## Development is based off the API's Postman collection. Download the Postman collection [here](https://app.bom.com/dashboard/detail-client_downloads) under the ```Arena API``` section. View the API documentation [here](https://app.bom.com/73.1.3-rc1/static/webhelp/full/en_US/ApplicationHelp.htm#html/api_requests.html%3FTocPath%3DArena%2520REST%2520API%7CEndpoints%7C_____0).