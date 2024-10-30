import data

# Write your functions for each part in the space below.

# Part 1
def create_rectangle(p1: Point, p2: Point) -> Rectangle:
    top_left_x = min(p1.x, p2.x)
    top_left_y = max(p1.y, p2.y)
    bottom_right_x = max(p1.x, p2.x)
    bottom_right_y = min(p1.y, p2.y)
    top_left = Point(top_left_x, top_left_y)
    bottom_right = Point(bottom_right_x, bottom_right_y)
    return Rectangle(top_left, bottom_right)

# Part 2
    def shorter_duration_than(d1: Duration, d2: Duration) -> bool:
    total_seconds_d1 = d1.minutes * 60 + d1.seconds
    total_seconds_d2 = d2.minutes * 60 + d2.seconds
    return total_seconds_d1 < total_seconds_d2


# Part 3


# Part 4


# Part 5


# Part 6
