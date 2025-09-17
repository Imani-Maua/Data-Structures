def burst_baloons(baloons):
    if len(baloons) == 0: return 0
    if len(baloons) == 1: return 1
    baloons.sort(key=lambda x: x[1])
    candidate = baloons[0][1]
    count = 1
    i = 1
    n = len(baloons)
    while i < n: 
        if baloons[i][0] > candidate:
            count += 1
            candidate = baloons[i][1]
        else:
            candidate = min(candidate, baloons[i][1])   
        i += 1
    return count






    
    


