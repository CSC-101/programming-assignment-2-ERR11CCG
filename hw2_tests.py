import data
import hw2
import unittest


# Write your test cases for each part below.
#Part 1 
 
class TestCases(unittest.TestCase):
p1 = Point(2, 2)
p2 = Point(10, 10)
rectangle = create_rectangle(p1, p2)
print(rectangle)

p1 = Point(3, 5)
p2 = Point(8, 5)
rectangle = create_rectangle(p1, p2)
print(rectangle)

    # Part 2
d1 = Duration(3, 20)  
d2 = Duration(4, 0)   
print(shorter_duration_than(d1, d2))  

d3 = Duration(5, 0)
d4 = Duration(4, 30)
print(shorter_duration_than(d3, d4))  


    # Part 3


    # Part 4


    # Part 5


    # Part 6





if __name__ == '__main__':
    unittest.main()
