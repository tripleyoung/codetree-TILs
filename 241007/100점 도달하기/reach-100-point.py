n = int(input())
str=""
for i in range(n, 101):
    if(i>=90):
        str+="A"
    elif(i>=80):
        str+="B"
    elif(i>=70):
        str+="C"
    elif(i>=60):
        str+="D"
    else:
        str+="F"
    str+=" "
print(str)