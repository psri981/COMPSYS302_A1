import math

def sumHypotenuses(triangles):
    # Your code goes here
    finalSum = 0

    a = [item[0] for item in triangles]
    b = [item[1] for item in triangles]
    
    for i in range(len(triangles)):
        c = math.sqrt((a[i]*a[i]) + (b[i]*b[i]))
        finalSum += c

    return finalSum

print(sumHypotenuses([(3, 4),(5, 12)]))