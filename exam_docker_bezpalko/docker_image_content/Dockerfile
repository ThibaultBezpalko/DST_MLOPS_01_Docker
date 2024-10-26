# Partir d'une image ubuntu
FROM ubuntu:18.04

# Updater ubuntu puis installer python et pip puis installer la libriairie requests
RUN apt-get update && apt-get install python3-pip -y && pip3 install requests

# Définir une variable d'environnement LOG égale à 1
ENV LOG 1

# Récupérer le script python depuis la machine hôte
#ADD test_content.py /api/test_content.py

# Répertoire de travail
WORKDIR /api/

# Lancer le test python
CMD python3 test_content.py