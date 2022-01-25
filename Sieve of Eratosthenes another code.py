n = int(input())
prime = [True for i in range(n+1)]
p = 2
while p*p <= n:
    if prime[p] == True:
        for k in range(p*p, n+1, p):
            prime[k] = False
    p += 1
for j in range(2, n+1):
    if prime[j]:
        print(j, end=' ')
        
 '''
 
 Input => 50
 Output => 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
 
 Time Complexity => O(n*log(log(n)))
 Auxiliary Space => O(n)
 
 '''
