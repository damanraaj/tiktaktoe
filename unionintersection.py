def intersect(x,y):
    return set(x)&set(y)

def union(x,y):
    out=[]
    x=set(x)
    y=set(y)
    out=list(x&y)
    return out
