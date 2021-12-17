#Input მიღებული სტრინგიდან ადგენს მატრიცას:

def makeGrid(inp):
    inp = inp.replace(' ', '')
    inp = inp.split('\n')
    grid = list(map(lambda x: list(x), inp))
    return grid

#განსაზღვრავს მდგომარეობას მოცემულ მომენტში (ეძებს, რა პოზიციებზეა ბომბები)

def makeState(grid):
    len_i = len(grid)
    len_j = len(grid[0])
    state = []
    for i in range(len_i):
        for j in range(len_j):
            if grid[i][j] == '0':
                state.append((i,j))
    return state

def bomberMan(s, grid):
        
    if s <= 1:       
        return grid
    
    grid = makeGrid(grid)
    len_i = len(grid)
    len_j = len(grid[0])
    state = makeState(grid)
    
    
    k = 2
    while k<=s:
        if k%2 == 0:
            for i in range(len_i):
                for j in range(len_j):
                    grid[i][j] = '0'
        else:
            for (i,j) in state:
                grid[i][j] = '.'
                if i-1 >= 0:
                    grid[i-1][j] = '.'
                if j-1 >= 0:
                    grid[i][j-1] = '.'
                if i+1 < len_i:
                    grid[i+1][j] = '.'
                if j+1 < len_j:
                    grid[i][j+1] = '.'
            state = makeState(grid)
        k+=1
            
    lastGrid = list(map(lambda x: ''.join(x), grid))
    lastGrid = '\n'.join(lastGrid)
        
    return lastGrid
                    
  
if __name__ == '__main__':              
                            
    grid = ". . . . . . . \n. . . 0 . . .\n. . . . 0 . .\n. . . . . . .\n00 . . . . .\n00 . . . . . "
#   grid = input('Grid: ') 
    n = int(input('Number of seconds: '))
    print(bomberMan(n,grid))
