import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from Player import *
from utils import *

#Pulls a player's stats from the HCIM pages
def getPlayerStats(name, deathTime, statOrder, kcOrder):
	player_url = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/hiscorepersonal?user1='
	playerStats = Player()

	playerStats.name = name
	playerStats.deathDate = deathTime

	try:
		session = HTMLSession()
		player_r = session.get(player_url+searchName(name))
		soup = BeautifulSoup(player_r.text, 'html.parser')
		for i in range(len(statOrder)):
			tag = soup.select('a[href="overall?table='+str(i)+'&user='+searchName(name)+'"]')
			if(len(tag) > 0):
				rank = tag[0].parent.find_next_sibling('td').text
				level = tag[0].parent.find_next_sibling('td').find_next_sibling('td').text
				exp = tag[0].parent.find_next_sibling('td').find_next_sibling('td').find_next_sibling('td').text

				rank = int(rank.replace(',', ''))
				level = int(level.replace(',', ''))
				exp = int(exp.replace(',', ''))
			else:
				rank = '--'
				level = '--'
				exp = '--'

			statI = statInfo()
			statI.rank = rank
			statI.level = level
			statI.exp = exp
			setattr(playerStats, statOrder[i], statI)

		for i in range(len(kcOrder)):
			#Increment i by 1 because kc table starts at 1, not 0
			tag = soup.select('a[href="overall?category_type=1&table='+str(i+1)+'&user='+searchName(name)+'"]')
			if(len(tag) > 0):
				rank = tag[0].parent.find_next_sibling('td').text
				score = tag[0].parent.find_next_sibling('td').find_next_sibling('td').text

				rank = int(rank.replace(',', ''))
				score = int(score.replace(',', ''))
			else:
				rank = '--'
				score = '--'

			kcI = kcInfo()
			kcI.rank = rank
			kcI.score = score
			setattr(playerStats, kcOrder[i], kcI)

		return playerStats

	except requests.exceptions.RequestException as e:
		print(e)