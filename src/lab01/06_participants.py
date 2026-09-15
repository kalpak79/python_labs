t = 0
f = 0
n = int(input())
for i in range(n):
    st = input()
    if st.split()[-1]=="True":t+=1
    else:f+=1
print(t,f)