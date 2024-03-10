#Solved by ChatGPT.........
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 초기 위치와 방향 설정 (0: 북, 1: 동, 2: 남, 3: 서)
        current_position = [0, 0]
        direction = 0  # 북쪽을 바라봄
        
        # 방향 전환을 위한 방향 벡터 설정
        direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        for ch in instructions:
            if ch == "L":
                direction = (direction - 1) % 4
            elif ch == "R":
                direction = (direction + 1) % 4
            else:  # "G"
                move = direction_vectors[direction]
                current_position[0] += move[0]
                current_position[1] += move[1]
        
        # 한 사이클 후에 시작 지점으로 돌아오거나, 북쪽을 바라보지 않으면 True
        return current_position == [0, 0] or direction != 0
                
            
        
                
                
                
        
        