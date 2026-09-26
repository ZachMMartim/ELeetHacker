class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        result = []

        for course, prereq in prerequisites: 
            graph[prereq].append(course)
            indegree[course] += 1

        queue = deque()
        
        for course in range(numCourses):
            if indegree[course] == 0:
                result.append(course) 
                queue.append(course)
        
        completed = 0

        while queue:
            currCourse = queue.popleft()
            completed += 1
            for nextCourse in graph[currCourse]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0:
                    queue.append(nextCourse)
                    result.append(nextCourse)

        if completed == numCourses:
            return result
        else: 
            return []



        

        