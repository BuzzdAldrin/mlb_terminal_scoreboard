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
	print("No Completed Games")
	numberOfFinishedGames = 0

try:
	numberOfInProgressGames = len(scoreboard['ig_game'])
except Exception:
	print("No In Progress Games")
	numberOfInProgressGames = 0


'''
'''
def get_games(scoreboard, gameType):
	#print("")
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
	return (True)




if (numberOfFinishedGames > 0):
	print("\nCompleted Games for " + str(month) + "/" + str(day) + "/" + str(year))
	print()
	get_games(scoreboard, 'go_game')



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