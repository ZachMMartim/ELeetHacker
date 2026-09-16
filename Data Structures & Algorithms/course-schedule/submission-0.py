class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        
        current_path = set()
        visited = set()
        i = 1
        def dfs(course):
            if course in current_path:
                return False
            if course in visited: 
                return True
            current_path.add(course)
            for crs in preMap[course]:
                if not dfs(crs):
                    return False
            current_path.remove(course)
            visited.add(course)
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
                







        