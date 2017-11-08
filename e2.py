import requests

yearid = []
with open("ELECTION_ID.txt", "r") as out:
    items = out.read().split('\n')
    for item in items:
        yearid.append(item.split())

addr = 'http://historical.elections.virginia.gov/elections/download/%s/precincts_include:0/'

for x in yearid:
    if len(x) < 2:
        continue

    resp = requests.get(addr % (yearid[1]))
    with open(yearid[0] + ".csv", "w") as out:
        out.write(resp.text)
