def function(a,low,high,n) :
  m=a[low]
  for i in range(low+1,high+1):
      if a[i]>m:
          m=a[i]
  return max(m,n)


def main():
    n=int(input(""))
    q=int(input(""))
    lowestLow=n
    highestHigh=0
    array=[int(x) for x in range(n+1)]
    for i in range(q):
        low,high,value=[int(x) for x in input("").split()]
        if low<lowestLow:
            lowestLow=low
        if high>highestHigh:
            highestHigh=high
        for i in range(low+1,high+1):
           array[i]+=value
    result=function(array,lowestLow,highestHigh,n)
    print(result)

if __name__=="__main__":
      main()
