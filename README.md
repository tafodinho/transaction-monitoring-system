- The following instructions below is going to get the whole system up and running

[-] Requirements
- Docker
- docker-compose

[-] Proceduer
- in DIR /TransactionTrackingSystem
- in file .env replace your Database credentials
- $ docker-compose up


- After running the commands above the web, api, and scheduler start running at once
- you can stop the scheduler from running by running
- $ docker stop transactiontrackingsystem_scheduler_1
- and start it back by running
- $ docker run transactiontrackingsystem_scheduler_1
- if you go to http://localhost:3000 you will see a new transaction being created every minutes



[-] API DOCS

- The API is consisted of
    * Database
    * Models
    * Schemas
    * WebSocket -> created with socketio
    * Routes -> which is found in main.py
    * Test

- The FASTAPI was choosen because it a new framework which in due time might replace Flask as it is faster that flask an provides additional new fancy features such a templating which can make boostraping a project a lot easier(this application was not boostraped with a template because it didn't need all of the other features that are provided by FATAPI templates)

- I use postgres database for the storage because it is a production ready database and I can easily deploy the application to production with the database

- The application only has one Model which is the Transaction model. This model is going to be use as a template to create the transactions table the database. The transaction model is expected to have a timestamp type of integer but instead I used a datetime object as this can easily be managed and converted to any form as need may be and i was also getting some errors that were taking long to fix when i used tpye integer instead

- The Schemas are going to be used to describe our request and response data formats. This is going to provide automatic validation. This also enables an openapi to be build automaticaly.

- There exist a socket server that is going be responsible for informing the front end application that a new transaction record has ben created and it should update its state

- The routes of the api are found in the main.py file this are the routes to which the our request from the scheduler and the web forntend will be directed

- SQLALCHEMY is used to serve as an ORM(object relational mapper) which manages some of the database operations more efficiently and with little effor

- An openApi documentation can be found at http://127.0.0.1:8000/docs when the application is running

- Could not finish writing test due to some errors that were taking too long to fix. But I am currently working on it


[-] WEB FRONTEND DOCS

- The Web Frontend was build with React TypeScript and contains the various components
    * TransactionList 
    * TransactionDetails 
    * TransactionSearch
    * App 

- The App component is the root of all other components and contains a custum navigation login which is used to switch between comoponents/screens

- The TransactionList component displays a list of all the transactions in the database and all of this items are clickable.

- TransactionDetails component displays the details about a particular transaction 

- TransactionSearch is the component that displays the list of transactions that are listed when you search a particular phrase. the search currently doesn't search by value as I was getting a type error in the backend that was taking a too long to debug and will be fixed as soon as possible 


* RUN SCHEDULER
- cd into scheduler/
- run python -m venv svenv
- run source svenv/bin/activate to activate virtual enviroment for scheduler
- run pip install -r requirements.txt