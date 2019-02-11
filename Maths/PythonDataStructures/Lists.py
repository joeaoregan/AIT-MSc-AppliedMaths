#!/usr/bin/env python3

players=['Simon','Mary','Louise','Tony']
print(players)

print(players[2])

print(players[1:3])

print('The number of players in the list: %d' %len(players))

players.sort()
print(players)

players.insert(3,'Karol')
print(players)

players.remove('Mary')
print(players)

players.sort()
print(players)

players.append('Batman')
players.append('Superman')
players.append('Wonder Woman')
print(players)

players.sort()
print('The numbers of players in the list is: %d' %len(players))

print('Displaying contents if a list using a loop')
for player in players:
    print(player)

del players[:]
print(players)