filetC = open("topologyCoordinates.txt", "r")
for line in filetC:
	xy_both = line.split(";")

coor = []
coorArray = []
x_coor = []
y_coor = []

for i in range(0,len(xy_both)):
        coor.append(xy_both[i].split(" "))
        
for i in range(len(coor)):
        for j in coor[i]:
                coorArray.append(j)
for i in range(0, len(coorArray)):
        if(i%2 == 0):
                x_coor.append(coorArray[i])
        else:
                y_coor.append(coorArray[i])
print((x_coor))
#print(len(y_coor))
