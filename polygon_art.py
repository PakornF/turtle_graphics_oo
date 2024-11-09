import turtle
import random


class Polygon:

    def __init__(self, num_side, size, orientation, location, color, border_size):
        self.num_side = num_side
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for i in range(self.num_side):
            turtle.forward(self.size)
            turtle.left(360 / self.num_side)
        turtle.penup()

    def move(self, location):
        self.location = location
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])


class PolygonArt:

    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer()
        turtle.colormode(255)

    def run(self):
        choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        for i in range(30):
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            reduction_ratio = 0.618
            num_level = 3

            if choice == 1:
                num_side = random.randint(3, 3)
                polygon = Polygon(num_side, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 2:
                num_side = random.randint(4, 4)
                polygon = Polygon(num_side, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 3:
                num_side = random.randint(5, 5)
                polygon = Polygon(num_side, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 4:
                num_side = random.randint(3, 5)
                polygon = Polygon(num_side, size, orientation, location, color, border_size)
                polygon.draw()
            elif choice == 5:
                num_side = random.randint(3, 3)
                embedded = EmbeddedPolygon(num_side, size, orientation, location, color, border_size, num_level,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 6:
                num_side = random.randint(4, 4)
                embedded = EmbeddedPolygon(num_side, size, orientation, location, color, border_size, num_level,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 7:
                num_side = random.randint(5, 5)
                embedded = EmbeddedPolygon(num_side, size, orientation, location, color, border_size, num_level,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 8:
                num_side = random.randint(3, 5)
                embedded = EmbeddedPolygon(num_side, size, orientation, location, color, border_size, num_level,
                                           reduction_ratio)
                embedded.draw()
            elif choice == 9:
                num_side = random.randint(3, 5)
                polygon = Polygon(num_side, size, orientation, location, color, border_size)
                polygon.draw()

                embedded = EmbeddedPolygon(num_side, size, orientation, location, color, border_size, num_level,
                                           reduction_ratio)
                embedded.draw()

        turtle.done()


class EmbeddedPolygon:

    def __init__(self, num_side, size, orientation, location, color, border_size, num_level, reduction_ratio):
        self.num_side = num_side
        self.size = size
        self.orientation = orientation
        self.original_location = location
        self.color = color
        self.border_size = border_size
        self.num_level = num_level
        self.reduction_ratio = reduction_ratio

    def draw(self):
        current_size = self.size
        for _ in range(self.num_level):
            offset_x = random.uniform(-current_size / 4, current_size / 4)
            offset_y = random.uniform(-current_size / 4, current_size / 4)
            location = [self.original_location[0] + offset_x, self.original_location[1] + offset_y]

            turtle.penup()
            turtle.goto(location[0], location[1])
            turtle.setheading(self.orientation)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()

            for i in range(self.num_side):
                turtle.forward(current_size)
                turtle.left(360 / self.num_side)
            turtle.penup()

            current_size *= self.reduction_ratio


def get_new_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


run = PolygonArt()
run.run()
