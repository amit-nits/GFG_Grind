for _ in range(int(input())):
    n = int(input()) 
    A = list(map(int,input().split()))
    A.sort()
    for i in range(1,n+1):
        if(i==n):
            print(n)
        elif(i!=A[i-1]):
            print(i)
            break
