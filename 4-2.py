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
builded_list.append(firestation)


for distance in distance_list:       #第二間:從第一間的距離list中抓最遠的
    if distance[first_firestation]==0:
        selected=distance
        second_firestation=selected.index(max(selected))
        builded_list.append(second_firestation)

next_list=[]
for distance in distance_list:
    df=distance[first_firestation]
    ds=distance[second_firestation]
    next=min(df,ds)
    next_list.append(next)

third_firestation=next_list.index(max(next_list))

print(first_firestation,second_firestation,third_firestation)
