import os
import requests
import time
from datetime import datetime


# Dictionnaire de test
dict_user_pwd = {
    'alice': 'wonderland',
    'bob': 'builder',
    'clementine': 'mandarine',
}

output = '''
============================
    Authentication test
============================

datetime = {dt}

request done at "/permissions"
| username="{user}"
| password="{pwd}"

expected result = 200
actual result = {status_code}

==>  {test_status}

'''

for user, pwd in dict_user_pwd.items():
    # requête
    for _ in range(5):
        try:
            r = requests.get(
                url='http://api:8000/permissions',
                params= {
                    'username': '{user}'.format(user=user),
                    'password': '{pwd}'.format(pwd=pwd)
                })
            # print(r.json()) # to test the test
            break
        except requests.exceptions.ConnectionError:
            print("Service not ready, retrying in 5 seconds...")
            time.sleep(5)


    # storing the current time in the variable
    dt = datetime.now()

    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(dt=dt, user=user, pwd=pwd, status_code=status_code, test_status=test_status))

    # impression dans un fichier
    if os.environ.get('LOG') == '1':
        with open('api_test.log', 'a') as file:
            file.write(output.format(dt=dt, user=user, pwd=pwd, status_code=status_code, test_status=test_status))