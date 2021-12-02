from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from faker import Faker
import random
import json
import time


BASE_URL="http://api:8000/api/v1.0"
ENDPOINT="/transactions"


fake = Faker()

def create_transaction():
    """
        Function which is called by the scheduler every
        minute to create a new record in the DB and update
        the confimed field from false to true after 10 seconds
        of creating.

        random attributes are generated from the faker library.
        a call to the create transactions edpoint is then initiated
        after which the system haults and waits for a response. If the 
        response is a success it then waits for 10 seconds before making
        a request for update the confirmed field. if any errors are caught
        in the process an error is printed in the console.
    """
    sender = fake.name()
    receiver = fake.name()
    value = random.randint(100, 1000)

    data = {
        "sender": sender,
        "receiver": receiver,
        "value": value
    }

    actions_list = []
    try:
        res = requests.post(BASE_URL+ENDPOINT, data=json.dumps(data))
        if res.status_code == 200:
            time.sleep(10)
            response = requests.patch(BASE_URL+ENDPOINT+"/"+res.json()['id'], data=json.dumps({"confirmed": True}))
            if not res.status_code == 200:
                print("Error updating confirmed to true")
        else:
            print("Error creating new transaction")
    except Exception as e:
        print(e)
    
print("HELLO WHY AM I NOT RUNNING")
scheduler = BlockingScheduler()
scheduler.add_job(create_transaction, 'interval', minutes=1)
scheduler.start()
