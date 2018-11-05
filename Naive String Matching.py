#Naive String Matching Algorithm

Text=input("Enter the text string: ")
Pattern=input("Enter the pattern string: ")
l1=list(Text)
l2=list(Pattern)

for i in range(len(l1)-len(l2)+1):
    n=i+len(l2)
    if l1[i:n]==l2[:]:
        print("Found with shift",i)
