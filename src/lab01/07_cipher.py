st = input()
step = 0
ind0 = []
ind1 = []
an = ""
for i in st:
    if i.isupper():ind0.append(st.index(i))
    if i.isnumeric():ind1.append(st.index(i))
step = (ind1[0]-ind0[0])+1

for i in range(ind0[0],len(st),step):
    an+=st[i]

print(an)