# 1. Prepare an array to count the indegrees and also hash table to keep the prerequisites needed for each course, when the indegrees is zero push into a queue  count ++ and BFS for the next dependent course and it's indegree in array, if the indegree gets to zero push it into the queue. traverse until queue is empty and check if count == numcourses
# TC: O(N)
# SC: O(N)
# Yes this worked in leetcode

from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        
        indegrees = [0]*numCourses
        dic = {i : [] for i in range(numCourses)}
        q = deque()
        count = 0
        for prerequisite in prerequisites:
            to = prerequisite[0]
            fro = prerequisite[1]

            indegrees[to] += 1
            dic[fro].append(to)

        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1

        while q:
            curr = q.popleft()
            edges = dic[curr]
            if not edges:
                continue
            for e in edges:
                indegrees[e] -= 1
                if indegrees[e] == 0:
                    q.append(e)
                    count += 1

        return count == numCourses
