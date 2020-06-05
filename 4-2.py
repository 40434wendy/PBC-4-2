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
    for i in range(city):
        times[i]=int(times[i])
        distance[i]=int(distance[i])
        accumulated=times[i]*distance[i]
        option+=accumulated
    option_list.append(option)

least_distance=min(option_list)
first_firestation=option_list.index(least_distance)
builded_list.append(first_firestation)

for distance in distance_list:
    if distance[first_firestation]==0:
        selected=distance
        second_firestation=selected.index(max(selected))
        selected[first_firestation]=9999
        builded_list.append(second_firestation)
