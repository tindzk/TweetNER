# TweetNER
This project provides an HTTP micro-service to recognise named entities in tweets. It is based on [tweepy](https://github.com/tweepy/tweepy), [spaCy](https://spacy.io/) and [Flask](http://flask.pocoo.org/).

## Dependencies
```shell
pip3 install -r requirements.txt
python3 -m spacy download en
```

## Configuration
Register a new Twiter app [here](https://apps.twitter.com/app/new) and set the following environment variables:

```shell
export TWITTER_CONSUMER_KEY=...
export TWITTER_CONSUMER_SECRET=...

export TWITTER_OAUTH_TOKEN=...
export TWITTER_OAUTH_TOKEN_SECRET=...
```

## Running
```shell
python3 classify.py

curl -i -H \
  "Content-Type: application/json" \
  -X POST \
  -d '{"tweet_id": "969287797214531590"}' \
  http://localhost:5000/classify
```

The result is as follows:

```http
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 45
Server: Werkzeug/0.14.1 Python/3.6.4
Date: Wed, 07 Mar 2018 18:21:13 GMT

[
  [
    "Jack Dorsey", 
    "PERSON"
  ]
]
```

## Licence
TweetNER is licensed under the terms of the Apache v2.0 licence.

## Contributors
* Tim Nieradzik
