a = []

for i in open ('sample1.csv'):
    res = i.split(",")
    i.append(int(res[8]))
    print("total",max(a))

c = []

for i in open ('sample1.csv'):
    res = i.split(",")
    if int(res[5]) == 100:
        c = c+1
    print("No of Hundreds ",c)

