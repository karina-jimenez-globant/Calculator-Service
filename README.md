# CALCULATOR SERVICE

Calculator API service allows to perform simple math operations on numbers. 

Available operations:
- Addition
- Subtraction
- Multiplication
- Division
 
## Getting started

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
$ git clone --- 
```

##Run the application 

```
$ make run   
```

##Run tests

```
$ make test
```
