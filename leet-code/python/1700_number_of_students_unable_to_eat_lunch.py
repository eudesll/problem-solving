class Solution:
  def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
    while sandwiches:
      if sandwiches[0] in students:
        students.remove(sandwiches[0])
        sandwiches.pop(0)
      else:
        break
      
    return len(students)
    # preferences = defaultdict(int)
    # for s in students:
    #   preferences[s] += 1
    
    # while len(students) > 0 and preferences[sandwiches[0]] > 0:
    #   student = students.pop(0)
    #   if student == sandwiches[0]:
    #     sandwiches.pop(0)
    #     preferences[student] -= 1
    #   else:
    #     students.append(student)
      
    # return len(students)