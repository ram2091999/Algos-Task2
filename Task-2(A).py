def function(a):
    stack=[]
    length=0
    if a[0]==">":
        return 0
    for e in a:
        if e=="<":
            stack.append("<")
            length+=1
        else:
            if not len(stack)==1:
                length+=1
                stack.pop()
            else:
                length+=1
                break
    if length==0:
        return 0
    elif (not length==0)and length<len(a):
        return length+function(a[length:])
    else:
        return length            


def main():
    n=int(input(""))
    a=[]
    for i in range(n):
        a.append(input(""))
    for e in a:
        print(function(e))

if __name__=="__main__":
    main()
