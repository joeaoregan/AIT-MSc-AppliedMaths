# 2. Data Structures % Data Compression
# Python Data Structures - S9

info = """This is a simple Python Script that demonstrates
sets and how they are used
===============================================
Superheroes in the DC universe: """

print (info)
DC = {'Superman', 'Batman', "Flash", 'Wonder Woman'}
print (DC)
answer1 = 'IronMan' in DC
answer2 = 'Flash' in DC
print ("Ironman is in the DC universe: {0}" .format(answer1))
print ("The Flash is in the DC universe: {0}" .format(answer2))

#alpha = set('abcdefghijklmnopqrstuvwxyz')
set1 = set('aaaaaabbbcdddddeffghiiiii')
set2 = set('abracadabra')
print ('Set 1 contains {0}' .format(sorted(set1)))
print ('Set 2 contains {0}' .format(sorted(set2)))
print ('Letters in Set1 but not Set2: {0}'.format(sorted(set1-set2)))
print ('Letters in Set1 or Set2 or both: {0}'.format(sorted(set1|set2)))
print ('letters in Set1 or Set2 but not both: {0}'.format(sorted(set1^set2)))
