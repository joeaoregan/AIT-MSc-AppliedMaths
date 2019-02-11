# 2. Data Structures % Data Compression
# Python Data Structures - S11

from collections import OrderedDict

info = """This is a simple Python Script that demonstrates
Dictionaries and how they are used
===============================================
Players and their score: """

scores = {'Karol':456,'Rita':987, 'Peter':963, 'Mary':741}
print(scores)
print ('Adding a player and score')
scores['Anne'] = 951
print (scores)
print ('Removing a player')
del scores['Karol']
print (scores)
print ("Players in the game include: {0}" .format(list(scores)))
bestPlayer= max(scores)
print ("The hgihest score int he game is {0} who has a score of {1}" .format(bestPlayer, scores[bestPlayer]))
print("Score Board")
for player, score in scores.items():
    print ("{0}\t{1}" .format(player, score))

print("In the next part we are going to sort the sictionary by ty the value decending")
ordered = (OrderedDict(sorted(scores.items(), key=lambda kv: kv[1], reverse=True)))
ranked = dict(ordered)
print("This generates a list of tuples that must be converted back to a dictionary")
print("Ranked Board")
for player, score in scores.items():
    print ("{0}\t{1}" .format(player, score))
