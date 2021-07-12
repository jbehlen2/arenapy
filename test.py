from src.arenapy import arenapy
import json

response = arenapy.login('brant.burkey@realmfive.com', 'y5DQQ^.6o`#4', 897540291)
sessionId = json.loads(response.text)['arenaSessionId']

try:
    response = arenapy.getItemSearch(sessionId, '100*')
except:
    arenapy.logout(sessionId)

print(response)