#Implementing Rabin Karp Algorithm
#Assuming that the text is numerical
# ∑={0,1,2,3,4,5,6,7,8,9} => d=10
#Note:In CLRS it's assumed that string starts from 1,hence the indices are lil bit different from the following ones

d=10
q=13
text=input('Enter the text string: ')
pattern=input('Enter the patterns string: ')
n=len(text)
m=len(pattern)
h=(d**(m-1))%q
p=0
t=0
#Preprocessing the data
for i in range(m):
    p=((d*p)+int(pattern[i]))%q
    t=((d*t)+int(text[i]))%q
#Matching the string
for i in range(n-m+1):
    if p==t:
        if pattern[:]==text[i:i+m]:
            print("Pattern found with shift",i)
    if i<n-m:                                       
        t=(d*(t-int(text[i])*h)+int(text[i+m]))%q     
        
Note:
1.)if i<n-m
This is important bcz in the last iteration we don't want to calculate the 't' value for the next m numbers,it will be out of bound.
2.)Time Complexity:Θ(m) preprocessing time, Θ((n-m+1)m) Matching time
