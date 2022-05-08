import tweepy
import yaml

def sendDeathTweet(deathFileLocation, playerName):
	#twitter_auth_keys = returnTwitterAuthKeys()
	with open(r'api_keys.yaml') as file:
		twitter_auth_keys = yaml.load(file, Loader=yaml.FullLoader)

	auth = tweepy.OAuthHandler(
		twitter_auth_keys['consumer_key'],
		twitter_auth_keys['consumer_secret']
		)
	auth.set_access_token(
		twitter_auth_keys['access_token'],
		twitter_auth_keys['access_token_secret'])
	api = tweepy.API(auth)

	# Upload image
	media = api.media_upload(deathFileLocation)

	tweet = playerName+" has died!"
	post_result = api.update_status(status=tweet, media_ids=[media.media_id])