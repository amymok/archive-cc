[![Build Status](https://travis-ci.org/amymok/miro.svg?branch=master)](https://travis-ci.org/amymok/miro) [![Coverage Status](https://coveralls.io/repos/github/amymok/miro/badge.svg?branch=master)](https://coveralls.io/github/amymok/miro?branch=master)

miro
====

A REST API that translate user supplied ID to an internally unique ID

## Features

* Get unique ID based on a Study ID and Study Subject ID

## Requirements

This project uses Python 3.6.  Other requirements can be retrieved and built with pip.

* django - Web framework
* djangorestframework - Rest API framework

## Setup & Running Locally
This instruction assumes that you are using Mac OS.  You can set up a virtual environment to isolate all your requirements for this project.  If you are not familiar with how to create an virtual environment, you can refer to [Python venv documentation](https://docs.python.org/3/library/venv.html) to learn how to do so.  You should then activate your virtual environment before starting the steps below.

### Clone
You will need to first clone the project to your local machine:
``` shell
git clone https://github.com/amymok/miro.git
```

### Dependencies
This project uses `requirements/base.txt` files for defining dependencies, so you can get up and running with `pip`:

```shell
cd miro
pip install -r requirements/base.txt

```

### Run local development server
You can now run the local development server
```shell
python manage.py runserver
```

## Basic API Usage
There's one endpoint in this project:
`GET /generate_miro_subject-id`

It takes two required query parameters:
- `study_id` : Study ID
- `study_subject_id`: Partcipant ID based in the study

example:
You can navigate to your browser or use your favorite API client and type a GET request:
http://127.0.0.1:8000/generate_miro_subject_id/?study_id=interesting-study.prestigious.edu&study_subject_id=20000

This will give you a json response back with one item:
- `miro_subject_id`: Miro unique ID based on study ID and study subject ID