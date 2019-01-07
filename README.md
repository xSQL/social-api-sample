# Social API sample

Requirements: Python 3.4+

# How to Use

1. Clone repo

2. Create & activate virtualenv

```bash
$ pyvenv venv
$ . venv/bin/activate
```

3. Install requirements

```bash 
(venv)$ pip install -r requirements.txt
```

4. Migrate db

```bash 
(venv)$ python src/manage.py migrate
```

4. Run server

```bash 
(venv)$ python src/manage.py runserver
```

4. Test with bot (optional)

```bash 
(venv)$ python bot/start.py
```


