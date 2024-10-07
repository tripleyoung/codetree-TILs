a , b = list(map(int,input().split()))
total_str=""
i=a
total_str+=str(i)
total_str+=" "
while(i<=b):
    if(i%2==0):
        i+=3
        if(i<=b):
            total_str+=str(i)
    else:
        i*=2
        if(i<=b):
            total_str+=str(i)
    total_str+=" "
print(total_str)