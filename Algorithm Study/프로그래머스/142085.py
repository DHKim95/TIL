def solution(n, k, enemy):
    
    def fight(enemy, n, k):
        # 무적권이 더 많으면 그냥 넘어간다.
        if k >= len(enemy):
            return True
        
        
        
        if sum(enemy) <= n:
            return True
        else:
            enemy.sort(reverse=True)
            for i in range(k):
                enemy[i] = 0
            if sum(enemy) <= n:
                return True
            else:
                return False
    
    left, right = 0, len(enemy)+1
    
    while left+1 < right:
        mid = (left + right) // 2
        if fight(enemy[:mid], n, k):
            left = mid
        else:
            right = mid
    
    answer = left
    return answer