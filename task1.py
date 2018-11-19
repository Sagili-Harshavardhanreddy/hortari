import collections
votes = ["john", "johnny", "jackie", "johnny", "john", "jackie","jamie", "jamie", "john","johnny", "jamie", "johnny","john"]

def winner(votes):
    votescount = collections.Counter(votes)
    dict = {}
    #print(votescount)
    for value in votescount.values():
        dict[value] = []
    for (key,value) in votescount.items():
        dict[value].append(key)
    
    #print(dict)
    
    maxVote = sorted(dict.keys(),reverse = True)[0]
    
    return print(sorted(dict[maxVote],reverse = True)[0])
    
    
    
    # for mem in sorted(dict[maxVote])
    #     print(mem)
    # if len(dict[maxVote])>1: 
    #     print(sorted(dict[maxVote])[0]) 
        
    # print(sorted(dict[maxVote]))
    # print(len(sorted(dict[maxVote])))
    
winner(votes)
