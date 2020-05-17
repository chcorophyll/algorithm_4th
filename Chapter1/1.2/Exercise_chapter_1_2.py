# # 1.21
# from random import uniform
# from Point2D import Point2D
#
#
# class RectanglePoint2D:
#
#     def __init__(self, num):
#         self.num = num
#         self.points = []
#
#     def random_point(self):
#         for i in range(self.num):
#             x = uniform(0, 1)
#             y = uniform(0, 1)
#             self.points.append(Point2D(x, y))
#
#     def dist_min(self):
#         point_dist = []
#         for i in range(len(self.points)):
#             for j in range(i+1, len(self.points)):
#                 temp_dist = self.points[i].dist(self.points[j])
#                 point_dist.append(temp_dist)
#         return min(point_dist)


# if __name__ == "__main__":
#     rect_point = RectanglePoint2D(50)
#     rect_point.random_point()
#     print(rect_point.dist_min())

# 1.2.2
# from Interval1D import Interval1D
# from random import uniform
#
# class IntersectValues():
#
#     def __init__(self, num):
#         self.num = num
#         self.intersect_vals = []
#
#     def random_interval(self):
#         for i in range(self.num):
#             x = uniform(0, 100)
#             y = uniform(0, 100)
#             self.intersect_vals.append(Interval1D(x, y))
#
#     def print_intersect(self):
#         for i in range(len(self.intersect_vals)):
#             for j in range(i+1, len(self.intersect_vals)):
#                 res = self.intersect_vals[i].interval_intersect(self.intersect_vals[j])
#                 if res:
#                     print("Interval_1: ", self.intersect_vals[i], "Interval_2: ", self.intersect_vals[j])
#
#
# if __name__ == "__main__":
#     intersect_vals = IntersectValues(50)
#     intersect_vals.random_interval()
#     intersect_vals.print_intersect()

# # 1.2.3
# from Interval1D import Interval1D
# from Interval2D import Interval2D
# from random import uniform
#
#
# class IntersectValues2D():
#
#     def __init__(self, num, val_min, val_max):
#         self.num = num
#         self.val_min = val_min
#         self.val_max = val_max
#         self.intervals = []
#
#     def random_interval2D(self):
#         for i in range(self.num):
#             x_low = uniform(self.val_min, self.val_max)
#             x_high = uniform(self.val_min, self.val_max)
#             y_low = uniform(self.val_min, self.val_max)
#             y_high = uniform(self.val_min, self.val_max)
#             x_interval = Interval1D(x_low, x_high)
#             y_interval = Interval1D(y_low, y_high)
#             self.intervals.append(Interval2D(x_interval, y_interval))
#
#     def print_intersect2D(self):
#         for i in range(len(self.intervals)):
#             for j in range(i+1, len(self.intervals)):
#                 res = self.intervals[i].interval_intersect2d(self.intervals[j])
#                 if res:
#                     print("Interval2D_1: ", self.intervals[i], "Interval2D_2: ", self.intervals[j])
#
#
# if __name__ == "__main__":
#     insect2D = IntersectValues2D(10, 2, 10)
#     insect2D.random_interval2D()
#     insect2D.print_intersect2D()

# 1.2.6
# class CircularRotation():
#
#     def find_circular_rotation(self, s1, s2):
#         if (s1 + s1).find(s2) != -1:
#             return True
#         else:
#             return False


# 1.2.9
# loop version
from Counter import Counter


def binary_search(arr, val):
    search_count = Counter(str(val))
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if val < arr[mid]:
            high = mid - 1
            search_count.increment()
        elif val > arr[mid]:
            low = mid + 1
            search_count.increment()
        else:
            search_count.increment()
            print(search_count.tally())
            return mid
    print(search_count.tally())
    return -1

