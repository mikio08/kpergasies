import random

a8roisma=0   
for i in range(1000):
    players = []   
    for i in range(100):
        nums=random.sample(range(1,81),5)
        if not (nums in players):
            players.append(nums)
             
    arithmoi = range(1,81)   
    random.shuffle(arithmoi)
    bingo = arithmoi[:5]    
    flag=False   
    fores=0     
    while flag==False:
        fores+=1
        for ari8mous in players:
            epituxies=0     
            for num  in ari8mous:
                if num in bingo:
                    epituxies+=1
            if epituxies==5:
                flag=True
        bingo.append(arithmoi.pop())    
    a8roisma+=fores

print a8roisma/1000     
