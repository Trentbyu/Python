def is_end_maze(maze, x, y):

    return maze[y][x] == 2

def is_valid_move(maze, curr_path, x, y):
    # Can't go outside of the maze boundary (assume maze is a square)
    if x > len(maze)-1 or x < 0:
        return False
    if y > len(maze)-1 or y < 0:
        return False
    # Can't go through a wall
    if maze[y][x] == 0:
        return False
    # Can't go if we have already been there (don't go in circles)
    if (x,y) in curr_path:
        return False
    # Otherwise, we are good
    return True

def solve_maze(maze, x=0, y=0, curr_path=None):

    
    if curr_path is None:
        curr_path = [(x,y)]

    if maze[y][x] !=0 or maze[y][x] != 2:
        if is_valid_move(maze, curr_path, x, y+1 ):
                if not is_end_maze(maze, x, y):
                    curr_path.append((x,y+1))
                    solve_maze(maze, x, y+1, curr_path)

    if maze[y][x] != 0 or maze[y][x] != 2:
        if is_valid_move(maze, curr_path, x, y-1 ):
                if not is_end_maze(maze, x, y):
                    curr_path.append((x,y-1))

                    solve_maze(maze, x, y-1, curr_path)

    if maze[y][x]!= 0 or maze[y][x] != 2:
        if is_valid_move(maze, curr_path, x+1, y):
            if not is_end_maze(maze, x, y):
                curr_path.append((x+1,y))

                solve_maze(maze, x+1, y, curr_path)
    if maze[y][x] != 0 or maze[y][x] != 2 :
        if is_valid_move(maze, curr_path, x-1, y ):
                if not is_end_maze(maze, x, y):
                    
                    curr_path.append((x-1,y))

                    solve_maze(maze, x-1, y, curr_path)


    if not is_end_maze(maze, x, y):
        curr_path.remove((x,y))
    
   
    if is_end_maze(maze,x ,y):
   
       print(curr_path, "\n")   

small_maze = [[1,1,1],[1,0,1],[1,1,2]]
solve_maze(small_maze)

big_maze = [
[1,0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0],
[1,1,1,1,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1,1],
[1,0,0,0,0,1,0,0,0,0,1,0,1,0,0,1,0,1,0,1],
[1,1,1,1,0,1,1,1,1,0,1,0,1,0,0,1,0,1,0,1],
[0,0,0,1,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],
[0,0,0,1,0,1,0,0,0,0,1,0,1,1,1,1,0,1,1,1],
[1,1,1,1,0,1,0,0,1,1,1,0,0,0,0,1,0,0,0,1],
[0,1,0,1,0,1,0,0,1,0,1,0,1,1,1,1,0,1,1,1],
[0,1,0,1,0,1,0,1,1,0,1,0,0,0,0,1,0,0,0,1],
[1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1],
[0,1,1,1,1,1,0,1,0,0,1,0,1,0,0,0,0,0,0,1],
[0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,0,0,0,0,1],
[0,1,0,0,0,0,0,1,0,0,1,0,1,0,1,1,1,1,1,1],
[0,1,0,0,0,1,1,1,0,0,1,0,1,0,0,0,1,0,0,1],
[1,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0],
[0,1,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,1,1,0],
[0,1,1,1,0,1,0,1,0,0,1,0,1,0,0,0,0,0,1,1],
[0,1,0,0,0,1,0,1,1,1,1,0,1,1,1,0,0,1,1,0],
[0,1,0,0,0,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],
[1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,0,1,2]]

solve_maze(big_maze)
