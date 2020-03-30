# MBTA #
## Prerequisites ##
* [Python 3.7.4](https://www.python.org/downloads/)
* [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)
* [git](https://git-scm.com/downloads)
* [flask](http://flask.pocoo.org/)

## Installation ##
To install requirements in a virtual environment begin by running

    $ virtualenv venv

Followed by installing requirements:

    $ pip install -r requirements.txt

This is a Flask application which comes with some built-in commands. To start this application, run 

    $ python app.py runserver
    
## Solution ##
This application is a web server which runs on `localhost:5000` and responds to following requests:

```GET /routes```

Will list all MBTA subway lines in following format

    {
        "response": [
            "ID: Red, NAME: Red Line",
            "ID: Mattapan, NAME: Mattapan Trolley",
            "ID: Orange, NAME: Orange Line",
            // and so on
        ]
    }
    
```GET /routes/<route_id>```
Will list all the stops for the given subway line. Where `route_id` is a valid route ID which could be obtained in the previous request. If invalid route ID is given such as `Purple` this end point will respond with 400 `Invalid route ID`

    {
        "response": [
            "ID: place-forhl, NAME: Forest Hills",
            "ID: place-grnst, NAME: Green Street",
            "ID: place-sbmnl, NAME: Stony Brook",
           // and so on
        ]
    }
