import tweepy
import yaml

def sendDeathTweet(deathFileLocation, player, bossKCNames, bossKCDispNames):
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

	MAX_TWEET_LENGTH = 280

	tweet = player.name+" has died!"
	tweet += "\nRank {} Overall with {:,} XP".format(player.overall.rank, player.overall.exp)
	firstKCLine = True
	inTweetThread = False
	replyToReply = False
	for i in range(len(bossKCNames)):
		kcRank = getattr(player, bossKCNames[i]).rank
		kcAmt = getattr(player, bossKCNames[i]).score
		bossDispName = bossKCDispNames[i]
	
		#Only display if ranked in top 200
		if(kcRank != '--'):
			if(int(kcRank) <= 200):
				if(firstKCLine):
					tweet += "\n--"
					tweet += "\nRank {} {} - {} KC".format(kcRank, bossDispName, kcAmt)
					firstKCLine = False
				else:
					#Check to ensure tweet isn't too long
					possibleTweet = tweet + "\nRank {} {} - {} KC".format(kcRank, bossDispName, kcAmt)
					if(len(possibleTweet) <= MAX_TWEET_LENGTH):
						tweet = possibleTweet
					else:
						if(inTweetThread == False):
							# Tweet what we have so far and create a thread for the rest
							original_tweet = api.update_status(status=tweet, media_ids=[media.media_id])
							tweet = "Rank {} {} - {} KC".format(kcRank, bossDispName, kcAmt)
							inTweetThread = True
						else:
							if(replyToReply == False):
								# Tweet what we have so far and continue the thread
								reply_tweet = api.update_status(status=tweet, 
										in_reply_to_status_id=original_tweet.id, 
										auto_populate_reply_metadata=True)
								tweet = "Rank {} {} - {} KC".format(kcRank, bossDispName, kcAmt)
								replyToReply = True
							else:
								# Tweet what we have so far and continue the thread
								reply_tweet = api.update_status(status=tweet, 
										in_reply_to_status_id=reply_tweet.id, 
										auto_populate_reply_metadata=True)
								tweet = "Rank {} {} - {} KC".format(kcRank, bossDispName, kcAmt)
	if(inTweetThread == False):
		post_result = api.update_status(status=tweet, media_ids=[media.media_id])
	else:
		if(replyToReply == False):
			reply_tweet = api.update_status(status=tweet, 
					in_reply_to_status_id=original_tweet.id, 
					auto_populate_reply_metadata=True)
		else:
			reply_tweet = api.update_status(status=tweet, 
					in_reply_to_status_id=reply_tweet.id, 
					auto_populate_reply_metadata=True)