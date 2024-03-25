spiral = [[1]]

def findIndex(arr, value):
    for i in range(0, len(arr)):
        for j in range(0, len(arr[0])):
            if arr[i][j] == value:
                return i, j
            
    return None

def createSpiral():
    n = 1
    x = 0
    y = 0

    for i in range(0, 4):
        mx = len(spiral)
        my = len(spiral[0])
        
        if not(0 <= y < len(spiral) and 0 <= x + 1 < len(spiral[y])):
            for i in range(y, my):
                spiral[i].append(n+1)
                n+=1
        
            spiral.append([])

            for i in range(0, mx+1):
                spiral[mx].insert(0, n+1)
                n+=1

            y, x = findIndex(spiral, n)

        else:
            spiral.append([])

            for i in range(0, mx+1):
                spiral[my].append(n+1)
                n+=1

            for i in range(my-1, -1, -1):
                spiral[i].append(n+1)
                n+=1

            y, x = findIndex(spiral, n)

    for i in spiral:
        print(i)


createSpiral()