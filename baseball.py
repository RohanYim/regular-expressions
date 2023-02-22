import sys
import re
import requests
import urllib3
urllib3.disable_warnings()


def calc_average(at_bats,hits):
    if at_bats == 0:
        return 0
    else:
        return hits / at_bats

url = 'https://classes.engineering.wustl.edu/cse330/content/cardinals/cardinals-1940.txt'
response = requests.get(url, verify=False)
text = response.text
pattern = r'^(\w+ \w+) batted (\d+) times with (\d+) hits and (\d+) runs$'
regex = re.compile(pattern, re.MULTILINE)

players = {}

for match in regex.finditer(text):
    name = match.group(1)
    at_bats = int(match.group(2))
    hits = int(match.group(3))
    if name not in players:
        players[name] = (at_bats,hits)
    else:
        temp1,temp2 = players[name]
        players[name] = (at_bats+temp1,hits+temp2)
        
averages = []
for player in players:
    average = calc_average(players[player][0],players[player][1])
    averages.append((player, average))

averages.sort(key=lambda x: x[1], reverse=True)

for name, average in averages:
    print(f"{name}: {average:.3f}")