def intersect(x,y):
    out=[]
    x=list(set(x))
    y=list(set(y))
    for i in x:
        if i in y:
            out.append(i)
    return out

def union(x,y):
    out=[]
    x=set(x)
    y=set(y)
    out=list(x&y)
    return out
