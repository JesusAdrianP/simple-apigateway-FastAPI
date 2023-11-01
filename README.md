# Simple API Gateway
This is a simple API Gateway make whit FastAPI

## Installation

To Run this project, you will need:

* Python 3.10 or higher
* Pip

See how to run it locally [here](#run-locally)

## Usage

Add a new json file name ```urls_config.json```, at the same level of the main.py file.

This json file should have the following structure.
```json
{
    "usersService": {
        "url": "http://users-service.com",
        "resource_path_identifier": "/users"
    },
    "usersAPIService": {
        "url": "http://users-api-service.com",
        "resource_path_identifier": "/users/api"
    },
    "chatService": {
        "url": "http://127.0.0.1:10000",
        "resource_path_identifier": "/chat"
    }
}
```

>NOTES: <br>
>   - Please **DONT** put a foward slash at the end of the urls.
>   - In the resource path identifier always start with a foward slash.


## Run Locally

You should first create the file `urls_config.json`, follow this [instructions](#usage)

Clone the project

```bash
 git clone https://github.com/juanbailon/simple-apigateway-FastAPI.git
```

Go to the project directory

```bash
 cd simple-apigateway-FastAPI
```

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

Start server

```bash
 uvicorn main:app --reload --port 8000
```
