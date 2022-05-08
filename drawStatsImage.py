from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageOps

#Draws an output image for a dead hcim o7
def drawStatsImage(deadGuy):
	img = Image.open('image_template/bg-lg.png')
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype('image_template/RuneScape-Fonts/ttf/RuneScape-Plain-12.ttf', 75)
	titlefont = ImageFont.truetype('image_template/RuneScape-Fonts/ttf/RuneScape-Plain-12.ttf', 70)
	kcfont = ImageFont.truetype('image_template/RuneScape-Fonts/ttf/RuneScape-Plain-12.ttf', 50)
	draw.text((50, 20), 'Final Stats for '+deadGuy.name+' on '+deadGuy.deathDate, (0,0,0), font=titlefont)
	column1Ind = 116
	columnIncrement = 168
	column2Ind = column1Ind + 1*(columnIncrement)
	column3Ind = column1Ind + 2*(columnIncrement)
	row1Ind = 97
	rowIncrement = 127
	row2Ind = row1Ind + 1*(rowIncrement)
	row3Ind = row1Ind + 2*(rowIncrement)
	row4Ind = row1Ind + 3*(rowIncrement)
	row5Ind = row1Ind + 4*(rowIncrement)
	row6Ind = row1Ind + 5*(rowIncrement)
	row7Ind = row1Ind + 6*(rowIncrement)
	row8Ind = row1Ind + 7*(rowIncrement)

	iconOffsetColumn = -55
	iconOffsetRow = 8
	totalLvlOffsetColumn = -60
	totalLvlTextOffsetRow = -50
	newIconSize = (50, 50)

	draw.text((column1Ind, row1Ind), str(deadGuy.attack.level), (0,0,0), font=font)
	attackIcon = Image.open('image_template/stat_icons/Attack_icon.png', 'r')
	attackIcon = attackIcon.resize(newIconSize)
	img.paste(attackIcon, (column1Ind+iconOffsetColumn, row1Ind+iconOffsetRow), attackIcon.convert('RGBA'))

	draw.text((column1Ind, row2Ind), str(deadGuy.strength.level), (0,0,0), font=font)
	strengthIcon = Image.open('image_template/stat_icons/Strength_icon.png', 'r')
	strengthIcon = strengthIcon.resize(newIconSize)
	img.paste(strengthIcon, (column1Ind+iconOffsetColumn, row2Ind+iconOffsetRow), strengthIcon.convert('RGBA'))

	draw.text((column1Ind, row3Ind), str(deadGuy.defence.level), (0,0,0), font=font)
	defenceIcon = Image.open('image_template/stat_icons/Defence_icon.png', 'r')
	defenceIcon = defenceIcon.resize(newIconSize)
	img.paste(defenceIcon, (column1Ind+iconOffsetColumn, row3Ind+iconOffsetRow), defenceIcon.convert('RGBA'))

	draw.text((column1Ind, row4Ind), str(deadGuy.ranged.level), (0,0,0), font=font)
	rangedIcon = Image.open('image_template/stat_icons/Ranged_icon.png', 'r')
	rangedIcon = rangedIcon.resize(newIconSize)
	img.paste(rangedIcon, (column1Ind+iconOffsetColumn, row4Ind+iconOffsetRow), rangedIcon.convert('RGBA'))

	draw.text((column1Ind, row5Ind), str(deadGuy.prayer.level), (0,0,0), font=font)
	prayerIcon = Image.open('image_template/stat_icons/Prayer_icon.png', 'r')
	prayerIcon = prayerIcon.resize(newIconSize)
	img.paste(prayerIcon, (column1Ind+iconOffsetColumn, row5Ind+iconOffsetRow), prayerIcon.convert('RGBA'))

	draw.text((column1Ind, row6Ind), str(deadGuy.magic.level), (0,0,0), font=font)
	magicIcon = Image.open('image_template/stat_icons/Magic_icon.png', 'r')
	magicIcon = magicIcon.resize(newIconSize)
	img.paste(magicIcon, (column1Ind+iconOffsetColumn, row6Ind+iconOffsetRow), magicIcon.convert('RGBA'))

	draw.text((column1Ind, row7Ind), str(deadGuy.runecraft.level), (0,0,0), font=font)
	runecraftIcon = Image.open('image_template/stat_icons/Runecraft_icon.png', 'r')
	runecraftIcon = runecraftIcon.resize(newIconSize)
	img.paste(runecraftIcon, (column1Ind+iconOffsetColumn, row7Ind+iconOffsetRow), runecraftIcon.convert('RGBA'))

	draw.text((column1Ind, row8Ind), str(deadGuy.construction.level), (0,0,0), font=font)
	constructionIcon = Image.open('image_template/stat_icons/Construction_icon.png', 'r')
	constructionIcon = constructionIcon.resize(newIconSize)
	img.paste(constructionIcon, (column1Ind+iconOffsetColumn, row8Ind+iconOffsetRow), constructionIcon.convert('RGBA'))

	draw.text((column2Ind, row1Ind), str(deadGuy.hitpoints.level), (0,0,0), font=font)
	hitpointsIcon = Image.open('image_template/stat_icons/Hitpoints_icon.png', 'r')
	hitpointsIcon = hitpointsIcon.resize(newIconSize)
	img.paste(hitpointsIcon, (column2Ind+iconOffsetColumn, row1Ind+iconOffsetRow), hitpointsIcon.convert('RGBA'))

	draw.text((column2Ind, row2Ind), str(deadGuy.agility.level), (0,0,0), font=font)
	agilityIcon = Image.open('image_template/stat_icons/Agility_icon.png', 'r')
	agilityIcon = agilityIcon.resize(newIconSize)
	img.paste(agilityIcon, (column2Ind+iconOffsetColumn, row2Ind+iconOffsetRow), agilityIcon.convert('RGBA'))

	draw.text((column2Ind, row3Ind), str(deadGuy.herblore.level), (0,0,0), font=font)
	herbloreIcon = Image.open('image_template/stat_icons/Herblore_icon.png', 'r')
	herbloreIcon = herbloreIcon.resize(newIconSize)
	img.paste(herbloreIcon, (column2Ind+iconOffsetColumn, row3Ind+iconOffsetRow), herbloreIcon.convert('RGBA'))

	draw.text((column2Ind, row4Ind), str(deadGuy.thieving.level), (0,0,0), font=font)
	thievingIcon = Image.open('image_template/stat_icons/Thieving_icon.png', 'r')
	thievingIcon = thievingIcon.resize(newIconSize)
	img.paste(thievingIcon, (column2Ind+iconOffsetColumn, row4Ind+iconOffsetRow), thievingIcon.convert('RGBA'))

	draw.text((column2Ind, row5Ind), str(deadGuy.crafting.level), (0,0,0), font=font)
	craftingIcon = Image.open('image_template/stat_icons/Crafting_icon.png', 'r')
	craftingIcon = craftingIcon.resize(newIconSize)
	img.paste(craftingIcon, (column2Ind+iconOffsetColumn, row5Ind+iconOffsetRow), craftingIcon.convert('RGBA'))

	draw.text((column2Ind, row6Ind), str(deadGuy.fletching.level), (0,0,0), font=font)
	fletchingIcon = Image.open('image_template/stat_icons/Fletching_icon.png', 'r')
	fletchingIcon = fletchingIcon.resize(newIconSize)
	img.paste(fletchingIcon, (column2Ind+iconOffsetColumn, row6Ind+iconOffsetRow), fletchingIcon.convert('RGBA'))

	draw.text((column2Ind, row7Ind), str(deadGuy.slayer.level), (0,0,0), font=font)
	slayerIcon = Image.open('image_template/stat_icons/Slayer_icon.png', 'r')
	slayerIcon = slayerIcon.resize(newIconSize)
	img.paste(slayerIcon, (column2Ind+iconOffsetColumn, row7Ind+iconOffsetRow), slayerIcon.convert('RGBA'))

	draw.text((column2Ind, row8Ind), str(deadGuy.hunter.level), (0,0,0), font=font)
	hunterIcon = Image.open('image_template/stat_icons/Hunter_icon.png', 'r')
	hunterIcon = hunterIcon.resize(newIconSize)
	img.paste(hunterIcon, (column2Ind+iconOffsetColumn, row8Ind+iconOffsetRow), hunterIcon.convert('RGBA'))

	draw.text((column3Ind, row1Ind), str(deadGuy.mining.level), (0,0,0), font=font)
	miningIcon = Image.open('image_template/stat_icons/Mining_icon.png', 'r')
	miningIcon = miningIcon.resize(newIconSize)
	img.paste(miningIcon, (column3Ind+iconOffsetColumn, row1Ind+iconOffsetRow), miningIcon.convert('RGBA'))

	draw.text((column3Ind, row2Ind), str(deadGuy.smithing.level), (0,0,0), font=font)
	smithingIcon = Image.open('image_template/stat_icons/Smithing_icon.png', 'r')
	smithingIcon = smithingIcon.resize(newIconSize)
	img.paste(smithingIcon, (column3Ind+iconOffsetColumn, row2Ind+iconOffsetRow), smithingIcon.convert('RGBA'))

	draw.text((column3Ind, row3Ind), str(deadGuy.fishing.level), (0,0,0), font=font)
	fishingIcon = Image.open('image_template/stat_icons/Fishing_icon.png', 'r')
	fishingIcon = fishingIcon.resize(newIconSize)
	img.paste(fishingIcon, (column3Ind+iconOffsetColumn, row3Ind+iconOffsetRow), fishingIcon.convert('RGBA'))

	draw.text((column3Ind, row4Ind), str(deadGuy.cooking.level), (0,0,0), font=font)
	cookingIcon = Image.open('image_template/stat_icons/Cooking_icon.png', 'r')
	cookingIcon = cookingIcon.resize(newIconSize)
	img.paste(cookingIcon, (column3Ind+iconOffsetColumn, row4Ind+iconOffsetRow), cookingIcon.convert('RGBA'))

	draw.text((column3Ind, row5Ind), str(deadGuy.firemaking.level), (0,0,0), font=font)
	firemakingIcon = Image.open('image_template/stat_icons/Firemaking_icon.png', 'r')
	firemakingIcon = firemakingIcon.resize(newIconSize)
	img.paste(firemakingIcon, (column3Ind+iconOffsetColumn, row5Ind+iconOffsetRow), firemakingIcon.convert('RGBA'))

	draw.text((column3Ind, row6Ind), str(deadGuy.woodcutting.level), (0,0,0), font=font)
	woodcuttingIcon = Image.open('image_template/stat_icons/Woodcutting_icon.png', 'r')
	woodcuttingIcon = woodcuttingIcon.resize(newIconSize)
	img.paste(woodcuttingIcon, (column3Ind+iconOffsetColumn, row6Ind+iconOffsetRow), woodcuttingIcon.convert('RGBA'))

	draw.text((column3Ind, row7Ind), str(deadGuy.farming.level), (0,0,0), font=font)
	farmingIcon = Image.open('image_template/stat_icons/Farming_icon.png', 'r')
	farmingIcon = farmingIcon.resize(newIconSize)
	img.paste(farmingIcon, (column3Ind+iconOffsetColumn, row7Ind+iconOffsetRow), farmingIcon.convert('RGBA'))

	draw.text((column3Ind+totalLvlOffsetColumn, row8Ind+totalLvlTextOffsetRow), 'Total:', (0,0,0), font=font)
	draw.text((column3Ind+totalLvlOffsetColumn, row8Ind), str(deadGuy.overall.level), (0,0,0), font=font)



	kciconOffsetColumn = -35
	kciconOffsetRow = 8
	kccolumn1Ind = 610
	kccolumnIncrement = 200
	kccolumn2Ind = kccolumn1Ind + 1*(kccolumnIncrement)
	kccolumn3Ind = kccolumn1Ind + 2*(kccolumnIncrement)
	kccolumn4Ind = kccolumn1Ind + 3*(kccolumnIncrement)
	kcrow1Ind = 97
	kcrowIncrement = 60
	kcnewIconSize = (30, 30)

	kcOrder = ["clueScrollsAll", "clueScrollsBeginner", "clueScrollsEasy", \
		   "clueScrollsMedium", "clueScrollsHard", "clueScrollsElite", "clueScrollsMaster", "soulWarsZeal", \
		   "riftsClosed", "abyssalSire", "alchemicalHydra", "barrowsChests", "bryophyta", "callisto", "cerberus", \
		   "cox", "coxCM", "chaosElemental", "chaosFanatic", "commanderZilyana", "corporealBeast", "crazyArchaeologist", \
		   "daggannothPrime", "daggannothRex", "daggannothSupreme", "derangedArchaeologist", "generalGraardor", \
		   "giantMole", "grotesqueGuardians", "hespori", "kalphiteQueen", "kingBlackDragon", "kraken", "kreearra", \
		   "krilTsutsaroth", "mimic", "nex", "nightmare", "phosanisNightmare", "obor", "sarachnis", "scorpia", \
		   "skotizo", "tempoross", "gauntlet", "corruptedGauntlet", "tob", "tobHM", "thermonuclearSmokeDevil", \
		   "tzKalZuk", "tzTokJad", "venenatis", "vetion", "vorkath", "wintertodt", "zalcano", "zulrah"]
	kcIconFilenames = ["Clue_scroll_all", "Clue_scroll_(Beginner)", "Clue_scroll_(Easy)", \
		   "Clue_scroll_(Medium)", "Clue_scroll_(Hard)", "Clue_scroll_(Elite)", "Clue_scroll_(Master)", "Lil'_creator", \
		   "Abyssal_protector", "Abyssal_orphan", "Ikkle_hydra", "Chest_(Barrows_open)", "Bryophyta's_essence", "Callisto_cub", "Hellpuppy", \
		   "Olmlet", "Metamorphic_dust", "Pet_chaos_elemental", "Ancient_staff", "Pet_zilyana", "Pet_corporeal_critter", "Crazy_archaeologist_chathead", \
		   "Pet_dagannoth_prime", "Pet_dagannoth_rex", "Pet_dagannoth_supreme", "Deranged_archaeologist_chathead", "Pet_general_graardor", \
		   "Baby_mole", "Noon", "Bottomless_compost_bucket", "Kalphite_princess_(2nd_form)", "Prince_black_dragon", "Pet_kraken", "Pet_kree'arra", \
		   "Pet_k'ril_tsutsaroth", "Mimic", "Nexling", "Little_nightmare", "Parasitic_egg", "Hill_giant_club", "Sraracha", "Scorpia's_offspring", \
		   "Skotos", "Tiny_tempor", "Youngllef", "Corrupted_youngllef", "Lil'_zik", "Sanguine_dust", "Pet_smoke_devil", \
		   "Infernal_cape", "Fire_cape", "Venenatis_spiderling", "Vet'ion_jr.", "Vorki", "Phoenix", "Smolcano", "Pet_snakeling"]

	kcNumRows = 16
	for i in range(kcNumRows):
		draw.text((kccolumn1Ind, kcrow1Ind+(i*kcrowIncrement)), str(getattr(deadGuy, kcOrder[i]).score), (0,0,0), font=kcfont)
		icon = Image.open('image_template/kc_icons/'+kcIconFilenames[i]+'.png', 'r')
		icon.thumbnail(kcnewIconSize)
		img.paste(icon, (kccolumn1Ind+kciconOffsetColumn, kcrow1Ind+(i*kcrowIncrement)+kciconOffsetRow), icon.convert('RGBA'))

	arrayOffset = 16
	for i in range(kcNumRows):
		draw.text((kccolumn2Ind, kcrow1Ind+(i*kcrowIncrement)), str(getattr(deadGuy, kcOrder[i+arrayOffset]).score), (0,0,0), font=kcfont)
		icon = Image.open('image_template/kc_icons/'+kcIconFilenames[i+arrayOffset]+'.png', 'r')
		icon.thumbnail(kcnewIconSize)
		img.paste(icon, (kccolumn2Ind+kciconOffsetColumn, kcrow1Ind+(i*kcrowIncrement)+kciconOffsetRow), icon.convert('RGBA'))

	arrayOffset = 32
	for i in range(kcNumRows):
		draw.text((kccolumn3Ind, kcrow1Ind+(i*kcrowIncrement)), str(getattr(deadGuy, kcOrder[i+arrayOffset]).score), (0,0,0), font=kcfont)
		icon = Image.open('image_template/kc_icons/'+kcIconFilenames[i+arrayOffset]+'.png', 'r')
		icon.thumbnail(kcnewIconSize)
		img.paste(icon, (kccolumn3Ind+kciconOffsetColumn, kcrow1Ind+(i*kcrowIncrement)+kciconOffsetRow), icon.convert('RGBA'))

	arrayOffset = 48
	for i in range(len(kcOrder)-arrayOffset):
		draw.text((kccolumn4Ind, kcrow1Ind+(i*kcrowIncrement)), str(getattr(deadGuy, kcOrder[i+arrayOffset]).score), (0,0,0), font=kcfont)
		icon = Image.open('image_template/kc_icons/'+kcIconFilenames[i+arrayOffset]+'.png', 'r')
		icon.thumbnail(kcnewIconSize)
		img.paste(icon, (kccolumn4Ind+kciconOffsetColumn, kcrow1Ind+(i*kcrowIncrement)+kciconOffsetRow), icon.convert('RGBA'))

	deathFileLocation = 'image_template/death_images/'+deadGuy.name+'.png'
	img.save(deathFileLocation)

	return deathFileLocation