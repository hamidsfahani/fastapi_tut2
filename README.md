# A Sample Fastapi Project

- use `python -m venv venv` to create a virtual environment 
- activate virtual environment: (`.\venv\Scripts\activate`)
- عe this command for installing the required libraries : `pip install -r requirements.txt`
- to start the project , please run the `main.py` file in `app` folder.
- line 7 in `main.py` creates the DB : 
```python 
models.Base.metadata.create_all(bind=engine))
```
