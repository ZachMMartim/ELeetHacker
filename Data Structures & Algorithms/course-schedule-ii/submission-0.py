class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prereq in prerequisites: 
            graph[prereq].append(course)
            indegree[course] += 1
        
        queue = deque()

        for course in range(numCourses): 
            if indegree[course] == 0:
                queue.append(course)

        completed = 0
        result = []
        while queue:
            currCourse = queue.popleft()
            result.append(currCourse)
            completed += 1
            for nextCourse in graph[currCourse]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
        if completed != numCourses:
            return []
        return result
        

        