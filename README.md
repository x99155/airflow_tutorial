# Comment j'ai appris à utiliser airflow

## Pré-requis
- Docker installé
- Docker compose installé

## Utilisation
- Demarrer docker
- `docker-compose up airflow-init` : initialiser la bdd
- `docker-compose up -d` : demarrer les autres services
- go to: localhost:8080/home

## Conseils d'apprentissage et crédit:
J'ai suivi ce tutoriel sur YouTube qui est très bien expliqué. Pas besoin de suivre l'intégralité,
si vous savez comprenez déjà comment construire un DAG et comment utiliser les opérateurs 'PythonOperators et BashOperators'
c'est déjà suffisant. Le reste viendra en forgeant lol.

Voici le lien vers le tuto: https://www.youtube.com/watch?v=K9AnJ9_ZAXE
