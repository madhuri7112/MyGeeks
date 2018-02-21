#https://www.geeksforgeeks.org/find-number-of-islands/
def main():
    inp = map(int, raw_input().strip().split(' '))
    num_rows = inp[0]
    num_columns = inp[1]
    #num_columns = input()

    input_matrix = []
    for i in range(num_rows):
       input_matrix.append(map(int, raw_input().strip().split(' ')))
    

    print find_num_islands(input_matrix, num_rows, num_columns)


def find_num_islands(input_matrix, rows, columns):
    
    num_islands = 0
    for i in range(rows):
      for j in range(columns):
         if (input_matrix[i][j] == 1):
              dfs( i, j, rows, columns, input_matrix)
              num_islands = num_islands + 1
    
    return num_islands 

def isValidCoordinate(i, j, rows, columns):
   if (i<rows and j<columns and i >=0 and j>=0):
      return True
   else:
      return False

def dfs(i, j, rows, columns, input_matrix):
    
     #Marking this coord as visited
     input_matrix[i][j] = -1
     neighbours = [(i+1, j-1), (i+1,j), (i+1, j+1), (i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1)]
     for neighbour in neighbours:
          if (isValidCoordinate(neighbour[0], neighbour[1], rows, columns) and input_matrix[neighbour[0]][neighbour[1]] == 1):
              dfs(neighbour[0], neighbour[1], rows, columns, input_matrix)

main()

