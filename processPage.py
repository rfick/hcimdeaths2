import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from getPlayerStats import *
from drawStatsImage import *
from sendDeathTweet import *
from utils import *

def processPage(page_url, numPages, statOrder, kcOrder, trackedPlayers, newTrackedPlayers):
	try:
		session = HTMLSession()

		for hiscore_page in range(numPages):
			print('Processing page {}/{}'.format(hiscore_page+1, numPages))

			page_r = session.get(page_url+str(hiscore_page+1))
			soup = BeautifulSoup(page_r.text, 'html.parser')
			tags = soup.find_all('tr', class_=lambda value: value and value.startswith("personal-hiscores__row"))
			for i in range(len(tags)):
				rank = tags[i].find_next('td').text
				rank = rank.strip('\n')
				name = tags[i].find_next('a').text
				name = cleanName(name)
				deadCheck = tags[i].find_all(class_='hiscore-death')

				# If player was in last check of tracked players
				if(name in trackedPlayers):
					if(len(deadCheck) > 0):
						newTrackedPlayers[name] = 1
						if(trackedPlayers[name] == 0):
							# If player is dead, and last time they weren't, send death tweet
							deathTime = deadCheck[0].attrs['title']
							deathTime = deathTime[13:30]
							print('#{} {} IS DEAD AT {}'.format(rank, name, deathTime))

							playa = getPlayerStats(name, deathTime, statOrder, kcOrder)
							deathFileLocation = drawStatsImage(playa)

							sendDeathTweet(deathFileLocation, playa.name)
					else:
						newTrackedPlayers[name] = 0
				else:
					if(len(deadCheck) > 0):
						newTrackedPlayers[name] = 1
					else:
						newTrackedPlayers[name] = 0
						
	except requests.exceptions.RequestException as e:
		print(e)