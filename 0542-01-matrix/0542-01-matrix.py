class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows_count = len(mat)
        cols_count = len(mat[0])
        
        max_distance = rows_count * cols_count
        # print(max_distance)
        distances_list = [[max_distance] * cols_count for _ in range(rows_count)] 
        # print(distances_list)
        queue = deque()
        
        for i in range(rows_count):
            for j in range(cols_count):
                if mat[i][j] == 0:
                    distances_list[i][j] = 0
                    queue.append((i, j))
        # print(distances_list)
        # print(queue)
        directions_list = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        #BFS start!!
        while queue:
            row, col = queue.popleft()
            for direction_row, direction_col in directions_list:
                new_row, new_col = row + direction_row, col + direction_col
                # print(f"new_row is {new_row}")
                # print(f"new_col is {new_col}")
                # list index out of range 방지용
                is_new_row_within_bounds = new_row >= 0 and new_row < rows_count
                is_new_col_within_bounds = new_col >= 0 and new_col < cols_count

                if is_new_row_within_bounds and is_new_col_within_bounds:
                    is_new_position_unvisited = distances_list[new_row][new_col] == max_distance
                    if is_new_position_unvisited:
                        distances_list[new_row][new_col] = distances_list[row][col] + 1 
                        queue.append((new_row, new_col))
        return distances_list