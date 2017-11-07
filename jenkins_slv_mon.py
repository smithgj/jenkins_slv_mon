import requests
import sys

try:
    target = 'http://us2-jenkins-1.adminsys.mrll.com:8080/computer/svc-us2p-too-12.adminsys.mrll.com/api/json?pretty=true'
    slv_data = requests.get(target, auth=('gsmithb', 'C@$@8927'))
    slv_data.raise_for_status()
except requests.HTTPError as e:
    print(e)
    sys.exit(1)
if (not (slv_data.json()).get('offline')) and (not(slv_data.json()).get('temporarilyOffline')):
    print ('Jenkins slave svc-us2p-too-12.adminsys.mrll.com is up')
else:
    print('Jenkins slave svc-us2p-too-12.adminsys.mrll.com is down')

input('Hit any key to exit')
