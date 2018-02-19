from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import simplejson as json
import sys

# with open('keychain.json') as f:
#  keychain = json.load(f)

# Go to http://apps.twitter.com and create an app.
# The consumer key and secret will be generated for you automatically
consumer_key='qvz9Op5IuQVCTClRL8XElbWwE'
consumer_secret='cwculhUloIPvllG1gE47VFpxVcHQb9ly9AwAPiFQYKS9612Ced'

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token='10569772-r6OTgi7D5cvpERzlyWhVb50liECeIrBrwWMqZsle5'
access_token_secret='u2V85W7YRpQDM8tbYqhvVjYN1rdJlF1Nswl01RyjfPGFd'

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        # print(data.id)
        tweet = json.loads(data)
        original = sys.stdout
        sys.stdout = open('C:/temp/twitter_output3.txt', 'a')
        print('-------')
        print(data)
        # print(tweet.keys())
        sys.stdout = original
        print('-------')
        print(tweet['id'])
        print(tweet['text'])
        # with open(str(tweet['id']), 'w') as f:
        #    json.dump(tweet, f, indent=1)
        # with open('')
        # json.dump()
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['#ai'])