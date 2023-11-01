# Simple API Gateway
This is a simple API Gateway make whit FastAPI

## Index
1. [Installation](#installation)
2. [Usage](#usage)
3. [Examples](#examples)
    * [example 1](#example-1)
    * [example 2](#example-2)
    * [example 3](#example-3)
4. [Run Locally](#run-locally)

<br>

## Installation

To Run this project, you will need:

* Python 3.10 or higher
* Pip

See how to run it locally [here](#run-locally)

## Usage

Add a new json file named ```urls_config.json```, at the same level of the main.py file.

This json file should have the following structure.
```json
{
    "usersService": {
        "url": "https://users-service.com",
        "resource_path_identifier": "/users"
    },
    "usersAPIService": {
        "url": "https://users-api-service.com",
        "resource_path_identifier": "/users/api"
    },
    "chatService": {
        "url": "http://127.0.0.1:10000",
        "resource_path_identifier": "/chat"
    }
}
```

> _**NOTES**_: 
> <br>
>   - Please **DONT** put a foward slash at the end of the urls.
>   - In the resource path identifier always start with a foward slash.

<br>

The API Gateway will foward the client request to the correct service/microservice base in the `resource_path_identifier`


<br>

## Examples
Lets assume that we have the `urls_config.json` file shown in the [usage section](#usage), and the our API Gateway is running here

    http://127.0.0.1:8000


### _Example 1_

So now lets say the client will makes a POST request like this one to the API Gateway.

    POST    http://127.0.0.1:8000/users/api/token


Now the API Gateway will foward the request to the correct service.

    POST    https://users-api-service.com/users/api/token


And then foward the service response back to the client.

<br>

### _Example 2_

The client will makes a GET request to the API Gateway

    GET     http://127.0.0.1:8000/users/3

Now the API Gateway will foward the request to the correct service.

    GET     https://users-service.com/users/3

And then foward the service response back to the client.

<br>

### _Example 3_

The client will make a PATCH request to the API Gateway, with the purpose of changing the chat room name

    PATCH     http://127.0.0.1:8000/chat/room/45

Now the API Gateway will foward the request to the correct service.

    PATCH     http://127.0.0.1:10000/chat/room/45

And then foward the service response back to the client.


<br>

## Run Locally

Clone the project

```bash
 git clone https://github.com/juanbailon/simple-apigateway-FastAPI.git
```

Go to the project directory

```bash
 cd simple-apigateway-FastAPI
```

<br>

Now you should create the file `urls_config.json` inside the project directory, follow this [instructions](#usage)

<br>


Create virtual enviroment

```bash
 python3 -m venv venv
```

Activate virtual enviroment

- Linux
    ```bash
     venv/bin/activate
    ```
- Windows
    ```bash
     venv\Scripts\activate
    ```

Install dependincies

```bash
 pip install -r requirements.txt
```
> <u>_**HINT:**_</u> 
> <br>
>  If you have any trouble installing the dependencies from the requirements file, you can do this instead.
> <br>
> <br>
> ` pip install fastapi "uvicorn[standard]" httpx`
    
<br>

Start server

```bash
 uvicorn main:app --reload --port 8000
```
