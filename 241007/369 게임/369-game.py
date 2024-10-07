n = int(input())
total_str=""
for i in range(1,n+1):
    j = str(i)
    if("3" in j or "6" in j or "9" in j or i%3==0):
        total_str+="0"
    else:
        total_str+=j
    total_str+=" "
print(total_str)