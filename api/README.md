* API SETUP
[-] Requirements
- python 3.6 and above
- postgresql

[-] Setup procedure
- cd into api/app/
- run python -m venv avenv
- run source avenv/bin/activate to activate virtual enviroment for api
- run pip install -r requirements.txt
- run uvicorn main:app --reload
- An openApi documentation can be found at http://127.0.0.1:8000/docs

API will now be available at http://127.0.0.1:8000

* RUN SCHEDULER
- cd into scheduler/
- run python -m venv svenv
- run source svenv/bin/activate to activate virtual enviroment for scheduler
- run pip install -r requirements.txt