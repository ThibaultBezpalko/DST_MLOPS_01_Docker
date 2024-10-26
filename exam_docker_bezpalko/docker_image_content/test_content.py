import os
import requests
import time
from datetime import datetime


# Dictionnaire de test
dict_user_pwd = {
    'alice': 'wonderland'
}

# Sentences to test
dict_sentences = {
    "positive": ["life is beautiful"],
    "negative": ["that sucks"]
}


# Liste de routes
routes = ['v1/sentiment', 'v2/sentiment']

output = '''
============================
    Content test
============================

datetime = {dt}

request done at "/{route}"
| username="{user}"
| password="{pwd}"
| sentence="{sentence}"

expected status code = 200
actual status code = {status_code}

expected sign = {expected_sign}
actual result = {actual_sign}

==>  {test_status}

'''

for user, pwd in dict_user_pwd.items():
    for route in routes:
        for sentiment, sentences in dict_sentences.items():
            for sentence in sentences:
                # requête
                for _ in range(5):
                    try:
                        r = requests.get(
                            url='http://api:8000/{route}'.format(route=route),
                            params= {
                                'username': '{user}'.format(user=user),
                                'password': '{pwd}'.format(pwd=pwd),
                                'sentence': '{sentence}'.format(sentence=sentence)
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

                # score de la phrase testée
                score = r.json()['score']

                # signe du score
                if score > 0:
                    actual_sign = "+"
                elif score < 0:
                    actual_sign = "-"
                else:
                    actual_sign = "Le score est nul."

                # affichage des résultats
                if status_code == 200:
                    if sentiment == "positive":
                        expected_sign = "+"
                        if score > 0:
                            test_status = 'SUCCESS'
                    if sentiment == "negative" :
                        expected_sign = "-"
                        if score < 0:
                            test_status = 'SUCCESS'
                else:
                    test_status = 'FAILURE'
                print(
                    output.format(dt=dt, route=route, user=user, pwd=pwd, sentence=sentence, score=score,\
                     expected_sign=expected_sign, actual_sign=actual_sign, status_code=status_code, test_status=test_status)
                )

                # impression dans un fichier
                if os.environ.get('LOG') == '1':
                    with open('api_test.log', 'a') as file:
                        file.write(output.format(dt=dt, route=route, user=user, pwd=pwd, sentence=sentence, score=score,\
                         expected_sign=expected_sign, actual_sign=actual_sign, status_code=status_code, test_status=test_status)
                        )