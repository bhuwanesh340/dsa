arr_2d = [[10,20,30,40],
          [15,25,35,45],
            [27,29,37,48],
            [32,33,39,50]]

def staircase_search(arr,key,n,m):
    if key < arr[0][0] or key > arr[n-1][m-1]:
        return (-1,-1)
    
    i = 0 # starting row
    j = m-1 # starting column
    while i<=n-1 and j>=0:
        if arr[i][j] == key:
            return (i,j)
        elif arr[i][j] > key:
            j -= 1 # move left column
        else:
            i += 1 # move down row

row,col = staircase_search(arr_2d, 80, len(arr_2d), len(arr_2d[0]))
if row == -1 and col == -1:
    print("Element not found")
else:
    print(f"Element found at index: ({row},{col})")