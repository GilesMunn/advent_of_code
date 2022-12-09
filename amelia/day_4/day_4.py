import numpy as np

with open("input.txt") as f:
    lines = f.readlines()

print("Task 1:")

def intersection(a, b):
    """
    intput lists a and b.
    return c, numbers that appear in both a and b
    """
    c = [value for value in a if value in b]
    for i in range(len(c)):
        c[i] = int(c[i])
    return c

#def contains(a,b):
    """
    """

 #   intersection(a,b)
  #  return

count = 0 # number of assignment pairs that conain each other.
for x in lines:
    x = x.split(",")
    a = x[0]
    a = a.split("-")
    a = np.linspace(int(a[0]), int(a[-1]), int(a[-1])-int(a[0])+1)
    a = a.tolist()

    b = x[-1].replace("\n", "")
    b = b.split("-")
    b = np.linspace(int(b[0]), int(b[-1]), int(b[-1])-int(b[0])+1)
    b = b.tolist()
    #print(a)
    #print(intersection(a,b))
    if intersection(a,b) == a or intersection(a,b) == b:
        count +=1
        #print("inclusive!")


    #print("elf a: ", a)
    #print("elf b: ", b)
#a = np.linspace(1, 52, 52) # start, stop, number of values

print("number of pairs where one fully contains the other: ", count)
print(" ")

print("Task 2:")

count_2 = 0 # number of assignment pairs with any overlap.
for x in lines:
    x = x.split(",")
    a = x[0]
    a = a.split("-")
    a = np.linspace(int(a[0]), int(a[-1]), int(a[-1])-int(a[0])+1)
    a = a.tolist()

    b = x[-1].replace("\n", "")
    b = b.split("-")
    b = np.linspace(int(b[0]), int(b[-1]), int(b[-1])-int(b[0])+1)
    b = b.tolist()
    #print(a)
    #print(intersection(a,b))
    if len(intersection(a,b)) != 0:
        #print(a,b,intersection(a,b))
        count_2 +=1
    
print("number of pairs with ANY overlap: ", count_2)