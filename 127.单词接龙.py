#
# @lc app=leetcode.cn id=127 lang=python3
#
# [127] 单词接龙
#

# @lc code=start
import collections
from gc import collect
from queue import Empty


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        nodeNum = 0
        wordId = dict()
        edge = collections.defaultdict(list)
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        for word in wordList:
            addEdge(word)
        addEdge(beginWord)
        if endWord not in wordId:
            return 0

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

        word_edge = collections.defaultdict(list)

        q, q_reverse = [(wordId[beginWord], 0)], [(wordId[endWord], 0)]
        # return (wordId[beginWord], wordId[endWord])
        d = dict() # 存储是否访问过的dict key : step
        d_reverse = dict()
        count = 0
        ans = 0
        word_order = []
        while  len(q) > 0 or len(q_reverse) > 0 and count < 1e7:
            count += 1
            # if len(q) < len(q_reverse): # 选择元素少的队列开始bfs
            if len(q) > 0:
                q_size = len(q)
                for _ in range(q_size):
                    node, step = q[0]
                    q.pop(0)
                    if node in d_reverse:    # 目标已经访问过了
                        ans = (d_reverse[node] + step) // 2 + 1
                        # return (d_reverse[node], step, node)
                        # ans = d_reverse[node] + step -1
                        # return "666"
                        return ans
                    d[node] = step
                    next_words = word_edge[node]
                    for word in edge[node]:  # 正常bfs
                        if word not in d:
                            # d[word] = step + 1
                            q.append((word, step + 1))
                
            
            if len(q_reverse) > 0:
            # else: 
                q_reverse_size = len(q_reverse)
                for _ in range(q_reverse_size):
                    node, step = q_reverse[0]                
                    q_reverse.pop(0)
                    word_order.append(node)
                    if node in d:    # 目标已经访问过了
                        ans = (d[node] + step) // 2 + 1
                        # ans = d[node] + step -1
                        # return (d[node], step, node)
                        return ans
                    d_reverse[node] = step
                    next_words = word_edge[node]
                    for word in edge[node]:  # 正常bfs
                        if word not in d_reverse:
                            # word_edge.append((node, word, step))
                            '''if word == 'yecij' and step == 2:
                                return (node ,check(word, node), word, step, word in d)'''
                            # d_reverse[node] = step + 1
                            q_reverse.append((word, step + 1))       
        return ans

# @lc code=end

