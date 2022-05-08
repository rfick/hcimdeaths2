import pickle
from pathlib import Path
from processPage import *

page_url = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/overall?table=0&page='

# 25 players per page
numPages = 80

# Only track top 200 for each boss KC
numPagesKC = 8

#Order in which stats appear in the HTML table
statOrder = ["overall", "attack", "defence", "strength", "hitpoints", "ranged", "prayer", "magic", "cooking", \
			 "woodcutting", "fletching", "fishing", "firemaking", "crafting", "smithing", "mining", "herblore", \
			 "agility", "thieving", "slayer", "farming", "runecraft", "hunter", "construction"]
kcOrder = ["bountyHunterHunter", "bountyHunterRogue", "clueScrollsAll", "clueScrollsBeginner", "clueScrollsEasy", \
		   "clueScrollsMedium", "clueScrollsHard", "clueScrollsElite", "clueScrollsMaster", "lms", "soulWarsZeal", \
		   "riftsClosed", "abyssalSire", "alchemicalHydra", "barrowsChests", "bryophyta", "callisto", "cerberus", \
		   "cox", "coxCM", "chaosElemental", "chaosFanatic", "commanderZilyana", "corporealBeast", "crazyArchaeologist", \
		   "daggannothPrime", "daggannothRex", "daggannothSupreme", "derangedArchaeologist", "generalGraardor", \
		   "giantMole", "grotesqueGuardians", "hespori", "kalphiteQueen", "kingBlackDragon", "kraken", "kreearra", \
		   "krilTsutsaroth", "mimic", "nex", "nightmare", "phosanisNightmare", "obor", "sarachnis", "scorpia", \
		   "skotizo", "tempoross", "gauntlet", "corruptedGauntlet", "tob", "tobHM", "thermonuclearSmokeDevil", \
		   "tzKalZuk", "tzTokJad", "venenatis", "vetion", "vorkath", "wintertodt", "zalcano", "zulrah"]

outFileName = 'trackedPlayers.pkl'
# If dicitonary of tracked players doesn't exist create a new blank one
if Path(outFileName).is_file():
	with open(outFileName, 'rb') as f:
		trackedPlayers = pickle.load(f)
else:
	trackedPlayers = {}

# 1 = Dead, 0 = Alive
newTrackedPlayers = {}

processPage(page_url, numPages, statOrder, kcOrder, trackedPlayers, newTrackedPlayers)

# Check kc pages
# table=13 -> Abyssal Sire
# table=60 -> Zulrah
firstKcTracked = 13
lastKcTracked = 60
for i in range(firstKcTracked, lastKcTracked+1):
	print('Processing kc table {}/{}'.format(i-firstKcTracked, lastKcTracked-firstKcTracked))
	kc_page_url = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/overall?category_type=1&table={}&page='.format(str(i))
	processPage(kc_page_url, numPagesKC, statOrder, kcOrder, trackedPlayers, newTrackedPlayers)

with open(outFileName, 'wb') as f:
	pickle.dump(newTrackedPlayers, f)