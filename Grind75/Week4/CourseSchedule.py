class CourseSchedule:

    class Graph:

        def __init__(self, prerequisites: List[List[int]], numNodes):
            self.numNodes = numNodes
            self.adjList = {}
            for course in prerequisites:
                if course[0] not in self.adjList:
                    self.adjList[course[0]] = {course[1]}
                else:
                    self.adjList[course[0]].add(course[1])
            self.keys = self.adjList.keys()

        def acyclic(self):
            visited = [0] * self.numNodes

            def cycleDfs(key: int):
                if visited[key] == -1:
                    return False
                if visited[key] == 1:
                    return True
                
                visited[key] = -1

                neighbors = self.adjList[key] if key in self.adjList else []
                for neighbor in neighbors:
                    if not cycleDfs(neighbor):
                        return False

                visited[key] = 1
                return True

            for key in self.keys:
                if not cycleDfs(key):
                    return False
            return True



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseGraph = self.Graph(prerequisites, numCourses)
        return courseGraph.acyclic()
