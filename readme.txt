## A project for news scraper and storing it in MongoDB

## Setup

> pip install -r requirements.txt

## Runing scraper

> python crawler/script.py http://www.example.com
> python crawler/script.py http://www.bbc.com

## Running API

> python api.py

endpoints -

1. "/" - help text
2. "/article" - get articles

example -

"/article?author=facebook"
"/article?author=facebook&domain=bbc.com"