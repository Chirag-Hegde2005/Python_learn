# tuple methods in python
coordinates = (10, 20)
print(coordinates[0])  
# coordinates[0] = 50  # This will raise an error because tuples are immutable
print(coordinates)
lists=[]
for i in coordinates:
    lists.append(i)
lists.insert(1, 50)
print(lists)
coordinates=()
for j in lists:
    coordinates += (j,)
print(coordinates)