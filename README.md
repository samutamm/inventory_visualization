
### Start server

```bash
cd server
# (optional) create and activate a virtualenvironment
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt
python server.py
```

Now Swagger API description is available in http://localhost:5000. (documentation is TODO)

Run server side tests :

```bash
cd server
python -m unittest test_server.py
```

Unittest module should come by default with Python.


### Start serving frontend

```bash
cd frontend
npm install
npm run serve
```

### TODO

- unit testing to frontend, for example following this https://frontstuff.io/unit-test-your-first-vuejs-component
- enable to modify inventories
    - add a up/down buttons for each line in table in frontend
    - POST path to server that modifys the data
- documentation

