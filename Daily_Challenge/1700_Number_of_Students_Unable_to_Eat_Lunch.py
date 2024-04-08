# 1700 - Number of Students Unable to Eat Lunch
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        number_of_square_students = sum(students)
        number_of_round_students = n - number_of_square_students

        activity = True
        while len(students) > 0 and (activity or number_of_square_students > 0 and number_of_round_students > 0):
            activity = False
            sandwichtype = sandwiches[0]
            if students[0] == sandwichtype:
                activity = True
                students.pop(0)
                sandwiches.pop(0)
                if sandwichtype == 1:
                    number_of_square_students -= 1
                else:
                    number_of_round_students -= 1
            else:
                students.append(students.pop(0))

        
        return len(students)
