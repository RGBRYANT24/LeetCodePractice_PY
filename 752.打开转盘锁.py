#
# @lc app=leetcode.cn id=752 lang=python3
#
# [752] 打开转盘锁
#
<<<<<<< HEAD
# https://leetcode.cn/problems/open-the-lock/description/
#
# algorithms
# Medium (52.76%)
# Likes:    563
# Dislikes: 0
# Total Accepted:    106.7K
# Total Submissions: 202.4K
# Testcase Example:  '["0201","0101","0102","1212","2002"]\n"0202"'
#
# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8',
# '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
# 
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
# 
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
# 
# 字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。
# 
# 
# 
# 示例 1:
# 
# 
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。
# 
# 
# 示例 2:
# 
# 
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：把最后一位反向旋转一次即可 "0000" -> "0009"。
# 
# 
# 示例 3:
# 
# 
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"],
# target = "8888"
# 输出：-1
# 解释：无法旋转到目标数字且不被锁定。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= deadends.length <= 500
# deadends[i].length == 4
# target.length == 4
# target 不在 deadends 之中
# target 和 deadends[i] 仅由若干位数字组成
# 
# 
#
=======
>>>>>>> 77f257da59e47a765bab387d08c497f75de950a4

# @lc code=start
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
<<<<<<< HEAD
=======
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



                    

>>>>>>> 77f257da59e47a765bab387d08c497f75de950a4
# @lc code=end

