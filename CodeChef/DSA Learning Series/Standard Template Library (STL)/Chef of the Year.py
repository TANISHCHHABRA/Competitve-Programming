n = input().split()

chef_country = {}
chef_vote = {}
country_vote = {}

for _ in range(int(n[0])):
    a = input().split()
    chef_country[a[0]] = a[1]
    
for _ in range(int(n[1])):
    a = input()
    if a in chef_vote:
        chef_vote[a] += 1
    else:
        chef_vote[a] = 1
    country = chef_country[a]
    if country in country_vote:
        country_vote[country] += 1
    else:
        country_vote[country] = 1
        
maxi = 0
s = ""
for i in country_vote:
    if country_vote[i] > maxi:
        maxi = country_vote[i]
        s = i
for i in country_vote:
    if maxi == country_vote[i]:
        if i < s:
            s = i
print(s)
maxi = 0
s = ""
for i in chef_vote:
    if chef_vote[i] > maxi:
        maxi = chef_vote[i]
        s = i
for i in chef_vote:
    if maxi == chef_vote[i]:
        if s > i:
            s = i
print(s)
