# Count num of islands. Diagonals are not allowed. Adjacents are allowed.
def numOfIsland(g):
    if not g:
        return 0
    res=0
    row = len(g)
    col = len(g[0])
    
    def check(r,c):
        if r<0 or r>=row or c<0 or c>=col or g[r][c] != 1:
            return 
        g[r][c] = 0
        check(r+1, c)
        check(r-1, c)
        check(r, c+1)
        check(r, c-1)

    
    for i in range(row):
        for j in range(col):
            if g[i][j] == 1:
                res += 1
                check(i, j)
    return res

    

g = [
    [1,1,0,1],
    [1,0,0,0],
    [0,0,1,1],
    [0,1,0,0]
]

print(numOfIsland(g))