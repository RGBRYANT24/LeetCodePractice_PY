#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
from queue import Empty


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if endWord not in wordList:
            return 0
        
        def check(w1, w2):   # 判断两个节点之间有没有边
            if len(w1) != len(w2):
                return False
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count += 1
                if count > 1:
                    return False
            return True

        if check(beginWord, endWord):
            return 2

        

        q, q_reverse = [(beginWord, 1)], [(endWord, 1)]
        d = dict() # 存储是否访问过的dict key : step
        count = 0
        ans = 0
        while  len(q) > 0 and len(q_reverse) > 0 and count < 1e7:
            count += 1
            # if len(q) < len(q_reverse): # 选择元素少的队列开始bfs
            if True:
                node, step = q[0]
                q.pop(0)
                if node in d:    # 目标已经访问过了
                    ans = d[node] + step
                    break
                for word in wordList:  # 正常bfs
                    if (word not in d) and (check(node, word)):
                        q.append((word, step + 1))
                        d[node] = step + 1

            if True:
            # else:
                node, step = q_reverse[0]
                q_reverse.pop(0)
                if node in d:    # 目标已经访问过了
                    ans = d[node] + step
                    break
                for word in wordList:  # 正常bfs
                    if (word not in d) and (check(node, word)):
                        q_reverse.append((word, step + 1))
                        d[node] = step + 1


        return ans - 1

# @lc code=end

