import itertools

def weeklyBudget(budget):
# Mapping weekly cost of newspaper to its name in a dictionary
    cost = {
    26:"TOI",
    20.5:"Hindu",
    34: "ET",
    10.5:"BM",
    18:"HT",
    };
    val=[26,20.5,34,10.5,18]
    newspaper=[]
# storing all possible combinations to a variable
    combination=list(itertools.combinations(val, 2))
    for i in combination:
        if sum(i)<=budget: #Fitering out the combinations based on the weekly budget
            newspaper.append(i)
    
    newsCombinations=[]
    for i in range(len(newspaper)):
        val1=newspaper[i][0]
        val2=newspaper[i][1]
        newsCombinations.append((cost[val1],cost[val2])) # Getting values for keys
    print(newsCombinations)


budget=int(input())
weeklyBudget(budget)



