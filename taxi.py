
N=int(input("Введите колчество сотрудников компании "))
distance=list(float (input("Введите расстояние до дома сотрудника в километрах "))for i in range(N))
taxi_fare=list (float (input("Введите тариф такси за проезд одного километра в рублях ")) for i in range(N))
res=[0 for i in range(N)]
for i in range(N):
    res[distance.index(min(distance))]=int(taxi_fare.index(max(taxi_fare)))+1
    distance[distance.index(min(distance))] = float(1001)
    taxi_fare[taxi_fare.index(max(taxi_fare))] = float(0)
    
print(res)

