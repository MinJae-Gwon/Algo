data= [1,2,3,4,5]
res=[0]*3
visited=[0]*5

def combi(deep):
    global res   
    
    if deep ==3:
        print(res)
        
        return

    for i in range(5):
        if visited[i] == 0:
            visited[i] =True
            res[deep] = data[i]
            combi(deep+1)
            visited[i] = 0
combi(0)


