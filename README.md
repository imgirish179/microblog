### Steps to setup the environment

- Install python
- Create virtual environment
- Install flask

### Creating and activating virtual environment

```
python -m venv venv
source venv/bin/activate
```

### Install flask in the virtual environment
`pip install flask`

### Link to flask documentation
[Official Documentation](https://flask.palletsprojects.com/en/stable/)

### Installing packages specified in the requirements
`pip install -r requirements.txt`

### Uninstalling all packages in the virtual environment
`pip freeze | xargs pip uninstall -y`

### Automatically generating the requirements file
`pip freeze > requirements.txt`

### Flask shell
`flask shell`

### To run the flask app
```
export FLASK_APP=microblog.py
flask run
```