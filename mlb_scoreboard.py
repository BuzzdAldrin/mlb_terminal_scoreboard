#Jason Hammett
#MLB command line scoreboard
import datetime
import sys
import urllib.request
import xmltodict
from termcolor import colored, cprint
import colorama
import termcolor

teamColorDict = dict()
teamColorDict['Cardinals'] = ['white', 'on_red']
teamColorDict['Yankees'] = ['white', 'on_grey']
teamColorDict['Rays'] = ['white', 'on_cyan']
teamColorDict['Blue Jays'] = ['white', 'on_blue']
teamColorDict['Tigers'] = ['white', 'on_grey']
teamColorDict['Orioles'] = ['red', 'on_yellow']
teamColorDict['Red Sox'] = ['white', 'on_red']
teamColorDict['Marlins'] = ['white', 'on_cyan']
teamColorDict['Dodgers'] = ['white', 'on_blue']
teamColorDict['Pirates'] = ['grey', 'on_yellow']
teamColorDict['Reds'] = ['white', 'on_red']
teamColorDict['Braves'] = ['grey', 'on_red']
teamColorDict['Mets'] = ['white', 'on_blue']
teamColorDict['Nationals'] = ['white', 'on_red']
teamColorDict['Phillies'] = ['white', 'on_red']
teamColorDict['Twins'] = ['white', 'on_magenta']
teamColorDict['Indians'] = ['grey', 'on_red']
teamColorDict['White Sox'] = ['grey', 'on_white']
teamColorDict['Royals'] = ['white', 'on_magenta']
teamColorDict['Brewers'] = ['white', 'on_magenta']
teamColorDict['Giants'] = ['white', 'on_grey']
teamColorDict['Athletics'] = ['yellow', 'on_green']
teamColorDict['Mariners'] = ['grey', 'on_magenta']
teamColorDict['D-backs'] = ['white', 'on_magenta']
teamColorDict['Angels'] = ['white', 'on_red']
teamColorDict['Rangers'] = ['red', 'on_blue']
teamColorDict['Padres'] = ['white', 'on_magenta']
teamColorDict['Rockies'] = ['grey', 'on_magenta']
teamColorDict['Astros'] = ['white', 'on_red']
teamColorDict['Cubs'] = ['red', 'on_blue']

banner1 = "#   ____    ____  _____     ______      ______     ______    ___   _______     ________  ______      ___        _       _______     ______"
banner2 = "#  |_   \  /   _||_   _|   |_   _ \   .' ____ \  .' ___  | .'   `.|_   __ \   |_   __  ||_   _ \   .'   `.     / \     |_   __ \   |_   _ `."
banner3 = "#    |   \/   |    | |       | |_) |  | (___ \_|/ .'   \_|/  .-.  \ | |__) |    | |_ \_|  | |_) | /  .-.  \   / _ \      | |__) |    | | `. \ "
banner4 = "#    | |\  /| |    | |   _   |  __'.   _.____`. | |       | |   | | |  __ /     |  _| _   |  __'. | |   | |  / ___ \     |  __ /     | |  | | "
banner5 = "#   _| |_\/_| |_  _| |__/ | _| |__) | | \____) |\ `.___.'\\\  `-'  /_| |  \ \_  _| |__/ | _| |__) |\  `-'  /_/ /   \ \_  _| |  \ \_  _| |_.' / "
banner6 = "#  |_____||_____||________||_______/   \______.' `.____ .' `.___.'|____| |___||________||_______/  `.___.'|____| |____||____| |___||______.'  "

print(banner1)
print(banner2)
print(banner3)
print(banner4)
print(banner5)
print(banner6)
#print(str(len(sys.argv)))
# Must be either 0 or 3 command line arguments
if ((len(sys.argv) != 1) and (len(sys.argv) != 4)):
	print("Incorrect arguments\nEither provide no arguments for today's scores or provide Month Day Year for a specific date")
	sys.exit()
if(len(sys.argv) == 4):
	#Specific date
	month = int(sys.argv[1])
	day = int(sys.argv[2])
	year = int(sys.argv[3])

else:
	#current day
	date = datetime.date.today()
	month = date.month
	year = date.year
	day = date.day

#MLB game data
urlStr1 = "http://gd2.mlb.com/components/game/mlb/year_"
urlStr2 = "/month_"
urlStr3 = "/day_"
urlStr4 = "/scoreboard.xml"


#Formatting the url to today
finalUrl = urlStr1 + str(year) + urlStr2 + str(month).zfill(2) + urlStr3 + str(day).zfill(2) + urlStr4
print(finalUrl)
#Query the MLB website
response = urllib.request.urlopen(finalUrl)
responseDict = xmltodict.parse(response)

#Response is now an xml tag based dictionary
try:
	scoreboard = responseDict['scoreboard']
except e:
	print("No games today.")
	numberOfFinishedGames = 0
	numberOfInProgressGames = 0

#print(scoreboard)
try:
	numberOfFinishedGames = len(scoreboard['go_game'])
except Exception as e:
	#print(e)
	print("No Completed Games\n")
	numberOfFinishedGames = 0

try:
	numberOfInProgressGames = len(scoreboard['ig_game'])
except Exception:
	print("No In Progress Games\n")
	numberOfInProgressGames = 0


'''
'''
def get_games(scoreboard):

	
	gameType = 'go_game'
	if (numberOfFinishedGames > 0):
		print("Completed Games\n")
		print("Team\t\t\tRuns\tHits\tErrors\n")
		for game in scoreboard[gameType]:
			for team in game['team']:
				runs = team['gameteam']['@R']
				hits = team['gameteam']['@H']
				errors = team['gameteam']['@E']
				name = team['@name']
				spaces = " " * (10 - len(name))
				#cprint(name, teamColorDict[name][0], teamColorDict[name][1], end="")
				print(name, end="")
				print(spaces + "\t\t" + str(runs) + "\t" + str(hits) + "\t" + str(errors))
			print()
	gameType = 'ig_game'
	if (numberOfInProgressGames > 0):
		print("\nIn Progress Games\n")
		print("Team\t\t\tRuns\tHits\tErrors")
		for game in scoreboard[gameType]:
			#print(game.keys())
			print()
			status = game['game']['@status']
			startTime = game['game']['@start_time']
			#print(game['game'])
			if (status == "PRE_GAME" or status == "IMMEDIATE_PREGAME"):
				print("PREGAME\nStart Time = ", end="")
				print(startTime)
				for team in game['team']:
					runs = team['gameteam']['@R']
					hits = team['gameteam']['@H']
					errors = team['gameteam']['@E']
					name = team['@name']
					spaces = " " * (10 - len(name))
					#cprint(name, teamColorDict[name][0], teamColorDict[name][1], end="")
					print(name, end="")
					print(spaces + "\t\t" + str(runs) + "\t" + str(hits) + "\t" + str(errors))
			elif status == "IN_PROGRESS":
				inning = game['inningnum']
				outs = game['@outs']
				
				for team in game['team']:
					runs = team['gameteam']['@R']
					hits = team['gameteam']['@H']
					errors = team['gameteam']['@E']
					name = team['@name']
					spaces = " " * (10 - len(name))
					#cprint(name, teamColorDict[name][0], teamColorDict[name][1], end="")
					print(name, end="")
					print(spaces + "\t\t" + str(runs) + "\t" + str(hits) + "\t" + str(errors))
				print(inning['@half'] + str(inning['@inning']) + " " + str(outs) + " outs")
				try:
					pitcher = game['pitcher']
					print("P: " + pitcher['@name'])
				except KeyError as k:
					pass
				try:
					batter = game['batter']
					print("AB: " + batter['@name'])
				except KeyError as k:
					pass
				try:
					on_base = game['on_base']
					print("On Base: ")
					#print(len(game['on_base']))
					try:
						for base_runner in on_base:
							#print(base_runner)
							base_number = base_runner['@base']
							player = base_runner['player']
							print(str(base_number) + ": " + player['@name'])
					except TypeError as t:
						base_number = on_base['@base']
						player = on_base['player']
						print(str(base_number) + ": " + player['@name'])
					
				except KeyError as k:
					pass
			
	return (True)




get_games(scoreboard)


'''
print("Number of in progress games: " + str(numberOfInProgressGames))
print("Number of finished games: " + str(numberOfFinishedGames))
print(scoreboard['ig_game'])
print()

for game in scoreboard['ig_game']:
	print(game[''])


if (numberOfInProgressGames > 0):
	print(get_games(scoreboard, 'ig_game'))

'''
