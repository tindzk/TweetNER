import os
import spacy
import tweepy
from flask import Flask, request, jsonify

def twitter_auth():
    consumerKey    = os.environ['TWITTER_CONSUMER_KEY']
    consumerSecret = os.environ['TWITTER_CONSUMER_SECRET']

    oauthToken       = os.environ['TWITTER_OAUTH_TOKEN']
    oauthTokenSecret = os.environ['TWITTER_OAUTH_TOKEN_SECRET']

    auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
    auth.set_access_token(oauthToken, oauthTokenSecret)

    return auth

def twitter_fetch_tweet(auth, tweet_id):
    api   = tweepy.API(auth)
    tweet = api.get_status(tweet_id)
    return tweet.text

def text_classify_named_entities(nlp, text, entity_types):
    doc = nlp(text)
    return [(e.text, e.label_) for e in doc.ents if e.label_ in entity_types]

def main():
    auth = twitter_auth()
    nlp  = spacy.load('en')
    app  = Flask(__name__)

    @app.route('/classify', methods=['POST'])
    def classify():
        text     = twitter_fetch_tweet(auth, request.json['tweet_id'])
        entities = text_classify_named_entities(nlp, text, ['ORG', 'PERSON'])

        return jsonify(entities)

    app.run()

if __name__ == "__main__":
    main()
