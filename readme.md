# Q-CTRL-Api-for-Managing-Controls

API endpoints for managing controls using Q-CTRL api

## Getting Started

Install packages listed in requirements.txt file in project root directory or listed below in prerequisites

To run the server - 'python3 manage.py runserver'

See step by step section below for further details

## Prerequisites

- asgiref==3.2.3
- Django==3.0.1
- djangorestframework==3.11.0
- djangorestframework-jsonapi==3.0.0
- inflection==0.3.1
- libpq
- psycopg2==2.8.4 (to connect postgresql database to django app)
- django-filter==2.2.0
- django-filters==0.2.1
- django-postgres-copy==2.4.2
- pytz==2019.3
- sqlparse==0.3.0
- docker 
- postgres:9.5

## Step by step

- install python3
- activate virtual environment 'qctrlenv' located in the project root directory
- pip3 install django
- pip3 install django-filter
- pip3 install djangorestframework
- install docker desktop for mac (this includes docker-compose by default, else for other OS you need to install seperate)
- use 'docker-compose-up' to start up the postgres database container with the PostgreSQL configuration mentioned in 'docker-compose.yml' file located in project root directory as well
- use 'docker-compose ps' to verify the container is running
- use following docker commands to create database and give previliges
- docker exec -it YOUR_CONTAINER_NAME psql -U postgres -c "CREATE DATABASE control;"
- docker exec -it YOUR_CONTAINER_NAME psql -U postgres -c "CREATE USER admin SUPERUSER PASSWORD 'adminqctrl';"
- docker exec -it YOUR_CONTAINER_NAME psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE control TO admin;"
- replace 'YOUR_CONTAINER_NAME' with the name of the container created on your docker
- use 'brew install libpq' to make pg_config available
- update path variable with the location of 'libpq' 
- use 'pip3 install psycopg2' to install psycopg2 package that connects postgres database to django app
- python3 manage.py makemigrations
- use 'python3 manage.py migrate' to implement the changes and make database ready
- use 'python3 manage.py createsuperuser' with username 'admin' and password 'adminqtrl'
- pip3 install djangorestframework-jsonapi
- finally run 'python3 manage.py runserver' to start up and get running

## Definition
### Control

A control is an individual input a customer may employ to manipulate their quantum system using the Q-CTRL App

The following table represent the Control table schema

| Entity             | Data Type | Required | Description                                                                            |
| ------------------ | --------- | -------- | -------------------------------------------------------------------------------------- |
| name               | varchar   | Yes      | Name of the control                                                                    |
| type               | varchar   | Yes      | Type of the control and need to chosen from the given choices                          |
| maximum_rabi_rate  | float     | Yes      | Maximum achievable angular frequency of the Rabi cycle for a driven quantum transition |
| polar_angle        | float     | Yes      | An angle measured from the z-axis on the Bloch sphere                                  |

...


### APIs

The public api will be accessible via `/API/@path` where the `@path` determines what is the request for.

| #   | routes                  | Verbs     | Description                                           |
| --- | ----------------------- | -----     | ----------------------------------------------------- |
| 1   | `/API/controls`         | GET       | Get all the data of controls                          |
| 2   | `/API/controls/`        | POST      | Post a new data by sending json                       |
| 3   | `/API/controls/{id}`    | GET       | Get a specific control by sending id                  |
| 4   | `/API/controls/{id}/`   | PUT       | Update a control using id                             |
| 5   | `/API/controls/{id}/`   | DELETE    | Delete a specific data using id                       |
| 6   | `/API/export`           | GET       | Export bulk data of control in CSV format             |
| 7   | `/API/import`           | GET       | Export bulk data of control from CSV format file      |



### Acknowledgment

- Thank you Q-CTRL for giving me opportunity to explore my backend skills
- Contact me if any questions 