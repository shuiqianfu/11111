function find_path(grid, word):
    height = grid.rows
    width = grid.cols
    visited = set()
    path = []
    
    // 对于单词中的每个字母
    for each char in word:
        candidates = []
        if path is empty:
            // 第一个字母：找网格中所有char的位置
            for each point (x,y) in grid where grid[y][x] == char:
                candidates.add((x,y))
            // 选择最左上的点
            candidate = min(candidates, key=lambda p: (p.x, p.y))
        else:
            // 后续字母：从上一个点出发，找环面邻居中值为char且未访问的点
            last = path[-1]
            neighbors = [
                ((last.x-1) % width, last.y),   // 左
                ((last.x+1) % width, last.y),   // 右
                (last.x, (last.y-1) % height),  // 上
                (last.x, (last.y+1) % height)   // 下
            ]
            for each neighbor (x,y) in neighbors:
                if (x,y) not in visited and grid[y][x] == char:
                    candidates.add((x,y))
            // 选择最左上的邻居
            candidate = min(candidates, key=lambda p: (p.x, p.y))
        
        path.append(candidate)
        visited.add(candidate)
    
    return path
