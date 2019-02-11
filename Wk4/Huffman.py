"""
This script performs Huffman encoding on a string
"""


def Huffman(p):
    '''Return s Huffman code for an ensemble with distribution p'''
    #assert will test the condition that the probabilities sum to
    #1.  If this is not the case then an error is triggered
    assert(sum(p.values())>=0.9 and sum(p.values())<=1.1)  #Ensure probabilities sum to 1

    #Put in some information abou the zip function
    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p)==2):
        return dict(zip(p.keys(),['1','0']))

    # Create a new distribution my merging lowest probability pair
    p_prime = p.copy()
    a1, a2 = low_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1+a2] = p1+p2

    # Recurse and construct code on new distribution
    c = Huffman(p_prime)
    cala2 = c.pop(a1+a2)
    c[a1],c[a2] = cala2+'1', cala2+'0'

    return c

def low_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities'''
    assert(len(p)>=2) #Ensure there are at least 2 symbols in the dist
    sorted_p = sorted(p.items(), key=lambda x:x[1])
    print("P in ", p)
    print(sorted_p)
    print("============================================================")
    return sorted_p[0][0], sorted_p[1][0]


def loadTextFile():
    print("This is done on another file that will be added when i go back to work")


def main():
    #Example execution
    #ex = {'a' : 0.08, 'b': 0.10, 'c' : 0.12, 'd' : 0.15, 'e' : 0.20, 'f' : 0.35}
    #ex = {'a' : 0.1, 'b': 0.25, 'c' : 0.05, 'd' : 0.15, 'e' : 0.30, 'f' : 0.07, 'g':0.08}
    #ex = {'a' : 0.2, 'b': 0.1, 'c' : 0.15, 'd' : 0.25, 'e' : 0.30}
    #Next line is an exam question
    #ex = {'a' : 0.25, 'b': 0.05, 'c' : 0.15, 'd' : 0.275, 'e' : 0.284}
    ex = {'a': 0.0817, 'b' : 0.0145, 'c' : 0.0248, 'd' : 0.0431, 'e' : 0.1232, 'f' : 0.0209,
    	'g': 0.0182, 'h' : 0.0668, 'i' : 0.0689, 'j' : 0.001, 'k' : 0.008, 'l' : 0.0397, 'm' : 0.0277,
    	'n' : 0.0662, 'o': 0.0781, 'p' : 0.0156, 'q' : 0.0009, 'r': 0.0572, 's' : 0.0628, 't': 0.0905,
    	'u' : 0.0304, 'v': 0.0102, 'w' : 0.0264, 'x': 0.0015, 'y' : 0.0211, 'z': 0.0005}
    total = sum(ex.values())
    print (total)
    print(Huffman(ex))


if __name__ == "__main__":
    main()

