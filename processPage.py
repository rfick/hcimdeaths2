import requests
import time
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

			successfulGet = False
			while(successfulGet == False):
				page_r = session.get(page_url+str(hiscore_page+1))

				soup = BeautifulSoup(page_r.text, 'html.parser')

				# Check if Jagex is throttling requests
				tags = soup.find_all('p')
				if(tags[0].text == "Due to excessive use of the Hiscore system, your IP has been temporarily blocked."):
					print('Too many requests, getting temp IP banned! :(')
					print('Going to sleep for 10 minutes')
					#Pause for 10 minutes so we don't spam Jagex with requests that make them mad
					time.sleep(10*60)
				else:
					successfulGet = True

					# Process names on page
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
								if(trackedPlayers[name] == 0 and name not in newTrackedPlayers):
									# If player is dead, and last time they weren't (and their name hasn't already been checked - avoid double tweeting), send death tweet
									deathTime = deadCheck[0].attrs['title']
									deathTime = deathTime[13:30]
									print('#{} {} IS DEAD AT {}'.format(rank, name, deathTime))

									playa = getPlayerStats(name, deathTime, statOrder, kcOrder)
									deathFileLocation = drawStatsImage(playa)

									sendDeathTweet(deathFileLocation, playa.name)

								newTrackedPlayers[name] = 1
							else:
								newTrackedPlayers[name] = 0
						else:
							if(len(deadCheck) > 0):
								newTrackedPlayers[name] = 1
							else:
								newTrackedPlayers[name] = 0
						
	except requests.exceptions.RequestException as e:
		print(e)