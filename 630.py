import heapq


class Solution:
    def scheduleCourse(self, courses) -> int:
        courses.sort(key=lambda x: x[1])
        date = 0
        enrolled = []
        heapq.heapify(enrolled)
        for course in courses:
            if date + course[0] <= course[1]:
                date += course[0]
                heapq.heappush(enrolled, -course[0])
            elif enrolled and -enrolled[0] > course[0]:
                date += heapq.heappushpop(enrolled, -course[0])
                date += course[0]

        return len(enrolled)


a = Solution()
inp = [[5, 5], [4, 6], [2, 6]]
print(a.scheduleCourse(inp))
