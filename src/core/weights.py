import numpy as np

class Weights:
    def __init__(self):
        self.self = 0.1
        self.human = 0.1
        self.swap = 0.1
        self.role = 0.1
        self.value = 0.1
        self.love = 0.1

    def as_vector(self):
        return np.array([self.self, self.human, self.swap, self.role, self.value, self.love])

    def update_from_gradient(self, grad, eta=0.01):
        vec = self.as_vector() + eta * grad
        self.self, self.human, self.swap, self.role, self.value, self.love = vec
