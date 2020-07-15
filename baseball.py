import sys, os, re
if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

baseball_Regex = re.compile(r"^([A-Z][A-Za-z]*\s[A-Z][A-Za-z]*)\sbatted\s(\d+)\stimes\swith\s(\d+)\shits\sand\s(\d+)\sruns")
class Player:
    def __init__(self, name, bats, hits, runs, average):
        self.name = name
        self.bats = int(bats)
        self.hits = int(hits)
        self.runs = int(runs)
        self.average = average
    def updateValues(self, bats, hits, runs, average):
        self.bats = int(bats) + self.bats
        self.hits = int(hits) + self.hits
        self.runs = int(runs) + self.runs
        self.average = average + self.average
    def calc_average(self):
        return (int(self.hits)/int(self.bats))

players_dict = {}
with open(filename) as f:
    for line in f:
        matches = baseball_Regex.match(line.strip())
        if matches is not None:
            name = matches.group(1)
            bats = matches.group(2)
            hits = matches.group(3)
            runs = matches.group(4)
            average = 0
            if name in players_dict:
                players_dict[name].updateValues(bats, hits, runs, average)

            else:
                players_dict[name] = Player(name, bats, hits, runs, average)

for name in players_dict:
    player_average = players_dict[name].calc_average()
    players_dict[name].average = player_average

sorted_players = sorted(players_dict, key = lambda i: players_dict[i].average, reverse=True)


for name in sorted_players:
        print(name, end = '')
        print(": ", end = '')
        print('{:.3f}'.format(round(players_dict[name].average, 3)))
        
