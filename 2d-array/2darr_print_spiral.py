arr_2d = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def print_spiral(arr, rows, cols):
    startRow = 0
    endRow = rows-1
    startCol = 0
    endCol = cols-1

    # outer loop to traverse the boundary

    while startRow <= endRow and startCol <= endCol:
        for i in range(startCol, endCol+1):
            print(arr[startRow][i], end=" ")

        for i in range(startRow+1, endRow+1):
            # print("2nd loop: ",i)
            print(arr[i][endCol], end=" ")

        if startRow <= endRow:
            for i in range(endCol-1, startCol-1, -1):
                # print("3rd loop: ", i)
                print(arr[endRow][i], end=" ")

        if startCol <= endCol:
            for i in range(endRow-1, startRow, -1):
                print(arr[i][startCol], end=" ")


        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    print()

    return True

print_spiral(arr_2d, 4, 4)