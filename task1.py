from collections import Counter
votes = ["john", "johnny", "jackie", "johnny", "john", "jackie","jamie", "jamie", "john","johnny", "jamie", "johnny","john"]

def winner(votes):
    votescount = Counter(votes)
    dict = {}
    for value in votescount.values():
        dict[value] = []
    for (key,value) in votescount.items():
        dict[value].append(key)
    
    maxVote = sorted(dict.keys(),reverse = True)[0]
    
    return print(sorted(dict[maxVote],reverse = True)[0])
 
if __name__ == "__main__":
    winner(votes)
