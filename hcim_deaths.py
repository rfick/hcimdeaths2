import pickle
from datetime import datetime, timedelta
from pathlib import Path
from processPage import *
from apscheduler.schedulers.blocking import BlockingScheduler

def checkHiScores():
	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('Beginning hiscores check at {}...'.format(current_time))

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
			   "clueScrollsMedium", "clueScrollsHard", "clueScrollsElite", "clueScrollsMaster", "lms", "pvpArena", "soulWarsZeal", \
			   "riftsClosed", "abyssalSire", "alchemicalHydra", "barrowsChests", "bryophyta", "callisto", "cerberus", \
			   "cox", "coxCM", "chaosElemental", "chaosFanatic", "commanderZilyana", "corporealBeast", "crazyArchaeologist", \
			   "daggannothPrime", "daggannothRex", "daggannothSupreme", "derangedArchaeologist", "generalGraardor", \
			   "giantMole", "grotesqueGuardians", "hespori", "kalphiteQueen", "kingBlackDragon", "kraken", "kreearra", \
			   "krilTsutsaroth", "mimic", "nex", "nightmare", "phosanisNightmare", "obor", "sarachnis", "scorpia", \
			   "skotizo", "tempoross", "gauntlet", "corruptedGauntlet", "tob", "tobHM", "thermonuclearSmokeDevil", \
			   "toa", "toaExpert", \
			   "tzKalZuk", "tzTokJad", "venenatis", "vetion", "vorkath", "wintertodt", "zalcano", "zulrah"]
	kcDispNames = ["Bounty Hunter - Hunter", "Bounty Hunter - Rogue", "Clue Scrolls - All", "Clue Scrolls - Beginner", "Clue Scrolls - Easy", \
			   "Clue Scrolls - Medium", "Clue Scrolls - Hard", "Clue Scrolls - Elite", "Clue Scrolls - Master", "LMS", "PVP Arena", "Soul Wars Zeal", \
			   "Rifts Closed", "Abyssal Sire", "Alchemical Hydra", "Barrows Chests", "Bryophyta", "Callisto", "Cerberus", \
			   "COX", "COX CM", "Chaos Elemental", "Chaos Fanatic", "Commander Zilyana", "Corporeal Beast", "Crazy Archaeologist", \
			   "Daggannoth Prime", "Daggannoth Rex", "Daggannoth Supreme", "Deranged Archaeologist", "General Graardor", \
			   "Giant Mole", "Grotesque Guardians", "Hespori", "Kalphite Queen", "King Black Dragon", "Kraken", "Kree'arra", \
			   "K'ril Tsutsaroth", "Mimic", "Nex", "Nightmare", "Phosani's Nightmare", "Obor", "Sarachnis", "Scorpia", \
			   "Skotizo", "Tempoross", "Gauntlet", "Corrupted Gauntlet", "TOB", "TOB HM", "Thermonuclear Smoke Devil", \
			   "Tombs of Amascut", "Tombs of Amascut: Expert Mode", \
			   "Inferno", "Fight Caves", "Venenatis", "Vet'ion", "Vorkath", "Wintertodt", "Zalcano", "Zulrah"]

	outFileName = 'trackedPlayers.pkl'
	# If dicitonary of tracked players doesn't exist create a new blank one
	if Path(outFileName).is_file():
		with open(outFileName, 'rb') as f:
			trackedPlayers = pickle.load(f)
	else:
		trackedPlayers = {}

	# 1 = Dead, 0 = Alive
	newTrackedPlayers = {}

	processPage(page_url, numPages, statOrder, kcOrder, kcDispNames, trackedPlayers, newTrackedPlayers)

	# Check kc pages
	# table=13 -> Abyssal Sire
	# table=60 -> Zulrah
	firstKcTracked = 13
	lastKcTracked = 60
	for i in range(firstKcTracked, lastKcTracked+1):
		print('Processing kc table {}/{}'.format(i-firstKcTracked, lastKcTracked-firstKcTracked))
		kc_page_url = 'https://secure.runescape.com/m=hiscore_oldschool_hardcore_ironman/overall?category_type=1&table={}&page='.format(str(i))
		processPage(kc_page_url, numPagesKC, statOrder, kcOrder, kcDispNames, trackedPlayers, newTrackedPlayers)

	with open(outFileName, 'wb') as f:
		pickle.dump(newTrackedPlayers, f)

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")
	print('Hiscores check complete at {}.'.format(current_time))

#Begin in 1 minute, update every 2 hrs after
current_time = datetime.now()
start_time = current_time + timedelta(minutes=1)

scheduler = BlockingScheduler()
scheduler.add_job(checkHiScores, 'interval', hours=2, start_date=start_time)
scheduler.start()