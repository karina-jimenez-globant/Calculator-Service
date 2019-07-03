# CALCULATOR SERVICE

Calculator API service allows to perform simple math operations on numbers. 

Available operations:
- Addition
- Subtraction
- Multiplication
- Division
 
## Getting started
**Requirements**
You should have installed: 

1. Python2.7 
2. pip 

In case of having a different python version, you should have installed also: `virtualenv`


**Prerequisites**

API url: `/calculator/<function>`, where `function` describe which math operation is going to be to use,
it support `POST` requests only

API port: `8080`


The API accepts a JSON payload with the following structure: 

```
{
    "number_1": 10, 
    "number_2": 2
}
```

A successful response returns a JSON providing the result of the math function and a status code of `200`:
```
{
    "result": 12
}
```

An error response returns a JSON explaining why the error occur and the status code will correspond to the error return `(400, 500, 404)`: 
```
{
    "error": "The requested URL was not found on the server"
}
```


**Installing**

Clone the repo

```
$ git clone https://github.com/karina-jimenez-globant/Calculator-Service
$ cd Calculator-Service
```

**Install dependencies**
```
$ pip install -r requirements.txt
```

## Run the application 

```
$ python run_app.py  
```

## Run tests

```
$ pytest -v
```