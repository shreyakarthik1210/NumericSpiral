
import sys


# Input: in_data - handle to the input file
# Output: integer size of the spiral, odd integer between 1 and 100
def get_dimension(in_data):
    dim = in_data[0]

    # Get dimension from in_data, if invalid dimensions, raises exception
    try:
        dim = int(dim)
        if (dim <= 0 or dim > 99):
            raise ValueError
        if (dim%2 == 0):
            dim += 1
        return dim
    except ValueError:
        print("Invalid spiral size")
        quit()
        
    


# Input: n - size of spiral
# Output: returns a 2-D list representing a spiral

def create_spiral(n):
    current = n*n       # Determine and start with largest value in spiral given n
    array = [[0 for i in range(n)] for e in range(n)]       # create nxn 2D array filled with 0s

    # Set initial starting coordinates in 2D array
    x = 0
    y = n - 1

    for i in range(1, n*2):
        if (i%2 != 0):      #  If i is odd go left then down

            # Keep going left until bounday is hit or array already has value there
            while (y >= 0 and array[x][y] == 0):
                array[x][y] = current
                if (array[x][y-1] == 0):        
                    y = y - 1
                current -= 1
            x = x + 1       # Switch direction to go down

            # Keep going down until bounday is hit or array already has value there
            while(x <= n-1 and array[x][y] == 0):
                array[x][y] = current
                if(x + 1 < n and array[x+1][y] == 0):
                    x = x + 1
                current -= 1
            y = y + 1       # Switch direction to go right

        else:       # If i is not odd (even) go right then up

            # Keep going right until bounday is hit or array already has value there
            while (y <= n-1 and array[x][y] == 0):
                array[x][y] = current
                if(y+1 < n and array[x][y+1] == 0):
                    y = y + 1
                current -= 1
            x = x - 1        # Switch direction to go up

            # Keep going up until bounday is hit or array already has value there
            while(x > 0 and array[x][y] == 0):
                array[x][y] = current
                if (array[x-1][y] == 0):
                    x = x - 1
                current -= 1
            y = y - 1       # Switch direction to go left

    return array



# Input: in_data - handle to input file
#        spiral - the number spiral
# Output: calls method for each integer in file
def print_adjacent_sums(in_data, spiral):

    # Call the sum_adjacent_numbers if a valid int, otherwise continue for all values in in_data
    for i in range(1, len(in_data)):
        try:
            number = int(in_data[i].strip())
            if (number < 1):
                raise ValueError
            print(sum_adjacent_numbers(spiral, number))
        except ValueError:
            print("Invalid Data")
            continue




# Input: spiral - the number spiral
#        n - the number to find the adjacent sum for
# Output: integer that is the sum of the
#         numbers adjacent to n in the spiral
#         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    length = len(spiral)

    # Return 0 if n is not in spiral
    if (n > length**2):
        return 0
    
    # Find index value of n
    for i in range(length):
        for e in range(length):
            if (spiral[i][e] == n):
                x = i
                y = e
                break

    sum = 0     # Keep track of adjacent number sums

    # Check if the following indexes exist in spiral and if so add them to the sum
    if (x-1 >= 0):
        sum+=spiral[x-1][y]
        if (y-1 >= 0):
            sum+=spiral[x-1][y-1]
        if (y+1 < length):
            sum+=spiral[x-1][y+1]
    if (x+1 < length):
        sum+=spiral[x+1][y]
        if (y-1 >= 0):
            sum+=spiral[x+1][y-1]
        if (y+1 < length):
            sum+=spiral[x+1][y+1]
    if (y-1 >= 0):
        sum+=spiral[x][y-1]
    if (y+1 < length):
        sum+=spiral[x][y+1]

    return sum


# Input: spiral - the number spiral
# Output: printed spiral
def print_spiral(spiral):
    for i in range(0, len(spiral)):
        for j in range(0, len(spiral[0])):
            row_format = '{:>4}'
            print(row_format.format(spiral[i][j]), end='')
        print()




def main():
    debug = True
    if debug:
        in_data = open('spiral.in')
    else:
        in_data = sys.stdin

    # Read from file handle and store in list 
    in_data = in_data.readlines()

    # get the spiral size from the file
    size = get_dimension(in_data)
    # if valid spiral size
        
    if (size != -1):
        # create the spiral
        spiral = [[]]
        spiral = create_spiral(size)

        # use following line for debugging only
        print_spiral(spiral)

        # process and print adjacent sums
        print_adjacent_sums(in_data, spiral)

if __name__ == "__main__":
    main()
