#
# @lc app=leetcode.cn id=773 lang=python3
#
# [773] 滑动谜题
#

# @lc code=start
class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def to_str(b: List[List[int]]):
            s = ''
            for i in range(len(b)):
                for j in range(len(b[i])):
                    s += str(b[i][j])
            return s
        start = to_str(board)
        end = '123450'
        if start == end :
            return 0
        def transit(s):
            tmp_borad = []
            tmp = []
            result = []
            r, c = 0, 0 # 记录0所在的位置
            for i in range(3):
                tmp.append(int(s[i]))
                if s[i] == '0':
                    c = i
            tmp_borad.append(tmp)
            tmp = []
            for i in range(3, 6):
                tmp.append(int(s[i]))
                if s[i] == '0':
                    r, c = 1, i % 3
            tmp_borad.append(tmp)
            
            if r == 0 :
                tmp_borad[r + 1][c], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r + 1][c] # 0 向下交换
                result.append(to_str(tmp_borad))
                tmp_borad[r + 1][c], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r + 1][c]# 交换回去
            if r == 1:
                tmp_borad[r - 1][c], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r - 1][c] # 0 向上交换
                result.append(to_str(tmp_borad))
                tmp_borad[r - 1][c], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r - 1][c]# 交换回去
            if c < 2:
                tmp_borad[r][c + 1], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r][c + 1] # 0 向右交换
                result.append(to_str(tmp_borad))
                tmp_borad[r][c + 1], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r][c + 1]
            if c > 0:
                tmp_borad[r][c - 1], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r][c - 1] # 0 向左交换
                result.append(to_str(tmp_borad))
                tmp_borad[r][c - 1], tmp_borad[r][c] = tmp_borad[r][c], tmp_borad[r][c - 1]# 交换回去
            return result
        
        q, q_reverse = [(start, 0)], [(end, 0)]
        d = dict()
        d_reverse = dict()
        count = 0
        while (len(q) > 0 or len(q_reverse) > 0) and count < 1e6:
            q_size = len(q)
            for _ in range(q_size):
                count += 1
                node, step = q[0]
                q.pop(0)
                if node in d_reverse:
                    ans = d_reverse[node] + step
                    return ans
                next_nodes = transit(node)
                for s in next_nodes:
                    if s not in d:
                        q.append((s, step + 1))
                        d[s] = step + 1
            
            q_reverse_size = len(q_reverse)
            for _ in range(q_reverse_size):
                count += 1
                node, step = q_reverse[0]
                q_reverse.pop(0)
                if node in d:
                    ans = d[node] + step
                    return ans
                next_nodes = transit(node)
                for s in next_nodes:
                    if s not in d_reverse:
                        q_reverse.append((s, step + 1))
                        d_reverse[s] = step + 1
        
        return -1
            

# @lc code=end

