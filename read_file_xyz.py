import math
import copy


def read_xyz(filename):
    """
    Read the file , return a list
    """
    data = []
    with open(filename) as file:
        for line in file.readlines():
            data.append(line)
    return data
    #

a=read_xyz("sio2.xyz")
# print(a)
# print(len(a))

def ordering(n) :
    """
    Ordering the input list into a list with Atom name as string and its coordinate as floats
    """
    List = []
    for i in n :
        x = i.split()
        if len(x) > 2 :
            x[1] = float(x[1])
            x[2] = float(x[2])
            x[3] = float(x[3])
        List.append(x)
        # print(x)
    return List


b = ordering(a)
# ordering(a)

def atom(n):
    """
    Create a list with only atom's name
    """
    atom = []
    count = 0
    for i in n :
        count  += 1
        if count > 2 :
            atom.append(i[0])
    return atom


def coorx(n) :
    """
    Create a list including the coordinate on the x-axis of the atoms
    """
    coor = []
    count = 0
    for i in n :
        count  += 1
        if count > 2 :
            coor.append(i[1])
    return coor

def coory(n) :
    """
    Create a list including the coordinate on the y-axis of the atoms
    """
    coor = []
    count = 0
    for i in n :
        count  += 1
        if count > 2 :
            coor.append(i[2])
    return coor

def coorz(n) :
    """
    Create a list including the coordinate on the z-axis of the atoms
    """
    coor = []
    count = 0
    for i in n :
        count  += 1
        if count > 2 :
            coor.append(i[3])
    return coor

def distance(x,y):
    """
    Calculate the disctance between 2 atoms
    """
    dis = abs(math.sqrt(( x[1]-y[1])**2 + (x[2]-y[2])**2 + (x[3]-y[3])**2 ))
    return dis


# Split the list b into 2 list : 1 list only have the Si , another have the Oxygen
b1 = []
b2 = []
for i in b :
    if i[0] == "Si" :
         b1.append(i)
    if i[0] == "O" :
        b2.append(i)


# Calculate the number of Si and O
atoms = atom(b)
Silicon = []
Oxygen = []
for i in atoms :
    if i == "Si" :
        Silicon.append(i)
    else :
        Oxygen.append(i)
print("Number of Silicon:",len(Silicon))
print("Number of Oxygen:",len(Oxygen))

print(len(atom(b)))


#Calculate number of Si-O bonds, then calculate how many Oxygen surround 1 Silicon
link = []
for i in b1 :
    link.append(i)
    for u in b2 :
        if distance(i,u) < 2.2 :
            link.append(u)
print(len(link))
print("1 Silicon surrounded by:",int(len(link)/len(Silicon)),"Oxygen")

#Calculate the average SI-O bond's length
ave = 0
for i in b1 :
    for u in b2 :
        if distance(i,u) < 2.2 :
            ave += distance(i,u)
print("Average:",ave/len(link),"anstrom")


#Find the atoms have the max coordinate in each axis, and the Atoms have the min coordinate ( to be used as the coordinate origin if needed )
x = coorx(b)
y = coory(b)
z = coorz(b)
print("Max coordinate x-axis:",max(x),"Atom:",atoms[x.index(max(x))])
print("Max coordinate y-axis:",max(y),"Atom:",atoms[y.index(max(y))])
print("Max coordinate z-axis:",max(z),"Atom:",atoms[z.index(max(z))])

print("Atom have the min coordinate :",atoms[x.index(min(x))],min(x),min(y),min(z))



#Create a new crystalline structure
newx = float(abs(max(x)-min(x)))
newy = float(abs(max(y)-min(y)))
newz = float(abs(max(z)-min(z)))

# print(newx,newy,newz)
b_temp = copy.deepcopy(b)
for i in b_temp :
    if i[0] == "Si" or i[0] == "O" :
        i[1] += newx
        i[2] += newx
        i[3] += newx
    else:
        b_temp.remove(i)

b += b_temp

with open(r'double', 'w') as fp:
    for item in b:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')


