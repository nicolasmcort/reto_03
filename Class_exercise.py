import math

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
        self.length = 0
        self.slope = 0
        self.start = start
        self.end = end
        self.points = []

    def compute_length(self) -> float:
        self.length = math.sqrt((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)
        return self.length

    def compute_slope(self) -> float:
        slope_in_radians = math.atan2(abs(self.end.y - self.start.y), abs(self.end.x - self.start.x))
        self.slope = (slope_in_radians * 180) / math.pi # Convert to degrees
        return self.slope

    def compute_horizontal_cross(self) -> bool:
        # Returns True if the points are on opposite sides or are on the horizontal axis
        return self.start.y * self.end.y <= 0

    def compute_vertical_cross(self) -> bool:
        # Returns True if the points are on opposite sides or are on the vertical axis
        return self.start.x * self.end.x <= 0

    def discretize_line(self, n: int):
        self.points.clear()

        # Calculate the distance between points
        dx = (self.end.x - self.start.x) / (n - 1)
        dy = (self.end.y - self.start.y) / (n - 1)

        # Append the points to the list
        for i in range(n):
            new_x = self.start.x + i * dx
            new_y = self.start.y + i * dy
            self.points.append(Point(new_x, new_y))
            print(f"Points: ({new_x}, {new_y})")

class Rectangle:
    def __init__(self, method: int, *args):
        if method == 1:  # Bottom-left corner + width and height
            self.bottom_left, self.width, self.height = args
            self.center = Point(self.bottom_left.x + self.width / 2, self.bottom_left.y + self.height / 2)
            self.upper_right = Point(self.bottom_left.x + self.width, self.bottom_left.y + self.height)
        elif method == 2:  # Center + width and height
            self.center, self.width, self.height = args
            self.bottom_left = Point(self.center.x - self.width / 2, self.center.y - self.height / 2)
            self.upper_right = Point(self.center.x + self.width / 2, self.center.y + self.height / 2)
        elif method == 3:  # Two opposite corners (bottom-left and upper-right)
            self.bottom_left, self.upper_right = args
            self.width, self.height = self.upper_right.x - self.bottom_left.x, self.upper_right.y - self.bottom_left.y
            self.center = Point(self.bottom_left.x + self.width / 2, self.bottom_left.y + self.height / 2)
        elif method == 4:  # Four lines
            # Determine the vertical and horizontal lines
            vertical_lines = []
            horizontal_lines = []
            for line in args:
                slope = line.compute_slope()
                if slope == 90:
                    vertical_lines.append(line)
                elif slope == 0:
                    horizontal_lines.append(line)

            # Validate that there are 2 vertical lines and 2 horizontal lines
            if len(vertical_lines) != 2 or len(horizontal_lines) != 2:
                raise ValueError("There must be 4 lines")

            # Sort vertical and horizontal lines by their coordinates
            vertical_lines.sort(key=lambda l: min(l.start.x, l.end.x))
            horizontal_lines.sort(key=lambda l: min(l.start.y, l.end.y))

            # Ensure the lines intersect correctly
            x_condition = vertical_lines[0].start.x == horizontal_lines[0].start.x or vertical_lines[0].start.x == horizontal_lines[0].end.x
            y_condition = vertical_lines[1].end.y == horizontal_lines[1].start.y or vertical_lines[1].end.y == horizontal_lines[1].end.y

            if not x_condition or not y_condition:
                raise ValueError("The coordinates of the intersection points do not match")
            
            # Calculate two corners
            self.bottom_left = Point(vertical_lines[0].start.x, horizontal_lines[0].start.y)
            self.upper_right = Point(vertical_lines[1].start.x, horizontal_lines[1].start.y)
            
        # Common calculations for all methods
        self.upper_left = Point(self.bottom_left.x, self.upper_right.y)
        self.bottom_right = Point(self.upper_right.x, self.bottom_left.y)
        self.corners = [self.bottom_left, self.bottom_right, self.upper_left, self.upper_right]

    def compute_area(self) -> float:
        return self.width * self.height

    def compute_perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def compute_interference_point(self, point: Point) -> bool:
        # Check if the point is inside the rectangle
        return (self.bottom_left.x <= point.x <= self.upper_right.x) and (self.bottom_left.y <= point.y <= self.upper_right.y)
    
    # Repo with more details about this method: https://github.com/nicolasmcort/Ejercicio_clase_7.git
    def compute_interference_line(self, line_start: Point, line_end: Point) -> bool: 
        for corner in self.corners:
            # Calculate the difference in line coordinates
            dx = line_end.x - line_start.x 
            dy = line_end.y - line_start.y 

            # Check if the line is a point, then verify if that point is inside the rectangle
            if dx == 0 and dy == 0:
                return self.compute_interference_point(Point(line_start.x, line_start.y))
            
            # Calculate the value of t that represents the projection of the 'corner' point on the line   
            t = ((corner.x - line_start.x) * dx + (corner.y - line_start.y) * dy) / (dx**2 + dy**2)
            t = max(0, min(1, t)) # Parameter t should be within range [0, 1]

            # Calculete the projected point and check if it is within the rectangle
            closet_point = Point(line_start.x + t * dx, line_start.y + t * dy)
            if self.compute_interference_point(closet_point):
                return True
            
        return False
            
class Square(Rectangle):
    def __init__(self, method: int, *args):
        if method == 1:  # Bottom-left corner + side length
            super().__init__(1, args[0], args[1], args[1])  
        elif method == 2:  # Center + side length
            super().__init__(2, args[0], args[1], args[1])
        elif method == 3:  # Two opposite corners (square)
            super().__init__(3, args[0], args[1])
                    
# Example of use 
point1 = Point(0, 0)
point2 = Point(2, 0)
point3 = Point(2, 2)
point4 = Point(0, 2)

line1 = Line(point1, point2)
line2 = Line(point2, point3)
line3 = Line(point3, point4)
line4 = Line(point4, point1)

# Create a rectangle using the lines 
rectangle = Rectangle(4, line1, line4, line2, line3)
