import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.contents = [ball for ball, count in kwargs.items() for _ in range(count)]

    def __repr__(self):
        return f'{self.kwargs} {self.contents}'

    def draw(self, n):
        drawn_balls = []

        if n >= len(self.contents):
            drawn_balls.extend(self.contents)
            self.contents = []
            return drawn_balls

        for _ in range(n):
            ball = random.choice(self.contents)
            drawn_balls.append(ball)
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0  

    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        drawn_balls = temp_hat.draw(num_balls_drawn)


        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1


        success = True
        for ball, count in expected_balls.items():
            if drawn_counts.get(ball, 0) < count:
                success = False
                break

        if success:
            success_count += 1

    return success_count / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(
hat=hat,
expected_balls={'red':2,'green':1},
num_balls_drawn=5,
num_experiments=2000
)

print(probability)