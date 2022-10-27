#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def check(s: str):
            result = []
            for _ in range(len(s)):
                tmp = list(s)
                i = int(tmp[_])
                if i == 0:
                    tmp[_] = '9'
                    result.append(''.join(tmp))
                    tmp[_] = str(i)
                else:
                    tmp[_] = str(i - 1)
                    result.append(''.join(tmp))
                    tmp[_] = str(i)
                
                if i == 9:
                    tmp[_] = '0'
                    result.append(''.join(tmp))
                    tmp[_] = str(i)
                else:
                    tmp[_] = str(i + 1)
                    result.append(''.join(tmp))
                    tmp[_] = str(i)
            return result
        
        if '0000' in deadends:
            return -1
        
        if target == '0000':
            return 0
        q, q_reverse = [('0000', 0)], [(target, 0)] # 因为计算最终长度的时候不算起点
        d = dict()
        d_reverse = dict()
        count = 0
        bfs_list, re_bfs_list = [], []
        while (len(q) > 0 or len(q_reverse) > 0) and count < 1e5:
            
            q_size = len(q)
            q_reverse_size = len(q_reverse)
            if q_size > 0 :
                for _ in range(1):
                    count += 1
                    node, step = q[0]
                    q.pop(0)
                    bfs_list.append(node)
                    if node in d_reverse: # 反向bfs已经找到了
                        ans = d_reverse[node] + step
                        return ans
                    
                    next_list = check(node)
                    for s in next_list:
                        if s not in deadends and s not in d:
                            q.append((s, step + 1))
                            d[s] = step + 1
            
            
            if q_reverse_size > 0:
                count += 1
                node, step = q_reverse[0]
                q_reverse.pop(0)
                re_bfs_list.append(node)
                if node in d:
                    ans = d[node] + step
                    return ans
                
                next_list = check(node)
                for s in next_list:
                    if s not in deadends and s not in d_reverse:
                        q_reverse.append((s, step + 1))
                        d_reverse[s] = step + 1
                
        
        return -1



                    

# @lc code=end

