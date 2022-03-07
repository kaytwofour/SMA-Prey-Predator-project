"""Agents definition classes (Sheep, Wolf or GrassPatch)"""
from mesa import Agent
from prey_predator.random_walk import RandomWalker


class Sheep(RandomWalker):
    """
    A sheep that walks around, reproduces (asexually) and gets eaten.

    The init is the same as the RandomWalker.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        # self.reproduce = False

    def step(self):
        """
        A model step. Move, then eat grass and reproduce.
        """
        # ... to be completed
        self.random_move()
        self.energy -= 1
        if self.random.random() < self.model.sheep_reproduce:
            # self.reproduce = True
            a = Sheep(self.model.next_id(), self.pos, self.model, self.moore, energy=20)
            self.model.schedule.add(a)
            self.model.grid.place_agent(a, self.pos)


class Wolf(RandomWalker):
    """
    A wolf that walks around, reproduces (asexually) and eats sheep.
    """

    energy = None

    def __init__(self, unique_id, pos, model, moore, energy=None):
        super().__init__(unique_id, pos, model, moore=moore)
        self.energy = energy
        # self.reproduce = False

    def step(self):
        # ... to be completed
        self.random_move()
        self.energy -= 1
        if self.random.random() < self.model.wolf_reproduce:
            # self.reproduce = True
            a = Wolf(self.model.next_id(), self.pos, self.model, self.moore, energy=20)
            self.model.schedule.add(a)
            self.model.grid.place_agent(a, self.pos)


class GrassPatch(Agent):
    """
    A patch of grass that grows at a fixed rate and it is eaten by sheep
    """

    def __init__(self, unique_id, pos, model, fully_grown, countdown):
        """
        Creates a new patch of grass

        Args:
            grown: (boolean) Whether the patch of grass is fully grown or not
            countdown: Time for the patch of grass to be fully grown again
        """
        super().__init__(unique_id, model)
        # ... to be completed
        self.fully_grown = fully_grown
        self.countdown = countdown

    # def step(self):
    # ... to be completed
