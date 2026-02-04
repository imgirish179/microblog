## Creating a simple server
`python -m http.server`

option m stands for module

## Why do we need Flask
- The above HTTP server serves static files only
- Flask app serves dynamic content based on user inputs, database and business logics

## Introduction to Flask
- Light weight web application framework

## Flask Object
- Instance of Flask is a WSGI application
- The first parameter to the Flask is import_name which is the name of the package
- static_folder (defauts to static) is the location of the folder where the static files are served
- template_folder (defaults to templates) is the location of the folder that contains templates

## Hello world page from Netflix
[humans.txt](https://www.netflix.com/humans.txt)

## View function
- Python function which are handlers of application routes
- Core of end point in flask terminology

To check the view function registered to the rule, open the flask shell

```
for rule in app.url_map.iter_rules():
    print(f"Endpoint: {rule.endpoint} | Methods: {rule.methods} | Rule: {rule.rule}")
```

## HTTP Methods
1. OPTIONS
2. HEAD
3. GET
4. POST
5. PUT
6. PATCH
7. DELETE

## Return type of view function

The return type of view function must be a string, dict, list, tuple with headers or status, response instance or WSGI callable

## Same rule vs same view function

We cannot define two view functions with the same name but we can have two rules with same name pointing to different view functions. The view function defined first will be executed when the rule is triggered

## Jinja templates bundled with Flask

- Jinja templates engine comes bundled with Flask
- Rendering is the operation that converts templates to complete HTML page
- `render_template()` function is used for rendering

## Response of API
1. Browser
2. Thunderclient or Postman
3. Curl request

## Curl commands
```
curl -I http://127.0.0.1:5000/
curl -v http://127.0.0.1:5000/
```

## Application Context
- current_app is the proxy to the application handling the current request
- Go to flask shell and check the following
```
from flask import current_app
current_app.name
current_app.url_map
current_app._get_current_object()
```

## Questions
1. If we define two view functions with the same name, will the app crash when we start the server or will the app crash when we hit the URL that maps to that duplicate view function?
2. When should we use current_app and g?
3. What is circular imports and how to avoid circular imports?
