city_firestation=input().split(",")
city=int(city_firestation[0])
firestation=int(city_firestation[1])
times=input().split(",")

option_list=[]
distance_list=[]
builded_list=[]
for j in range(city):
    distance=input().split(",")
    distance_list.append(distance)

    option=0
    for i in range(city):            #第一間:計算最短總路徑長
        times[i]=int(times[i])
        distance[i]=int(distance[i])
        accumulated=times[i]*distance[i]
        option+=accumulated
    option_list.append(option)

least_distance=min(option_list)
first_firestation=option_list.index(least_distance)
builded_list.append(first_firestation)


for distance in distance_list:       #第二間:從第一間的距離list中抓最遠的
    if distance[first_firestation]==0:
        selected=distance
        second_firestation=selected.index(max(selected))
builded_list.append(second_firestation)

compare_list=[]
next_list=[]
for m in range(firestation-2):      #接下去蓋
    for distance in distance_list:
        for k in builded_list:
            compare_list.append(distance[k])
        next=min(compare_list)
        next_list.append(next)
        compare_list=[]
    next_firestation=next_list.index(max(next_list))
    builded_list.append(next_firestation)
    next_list=[]

pick_distance=[]
min_list=[]
for distance in distance_list:     #總距離
    for p in builded_list:
        pick_distance.append(distance[p])
    min_distance=min(pick_distance)
    min_list.append(min_distance)
    pick_distance=[]

total=0
for n in range(city):
    total+=times[n]*min_list[n]

for q in range(len(builded_list)):
    builded_list[q]=str(builded_list[q]+1)

format=",".join(builded_list)
print(format+";"+str(total))
