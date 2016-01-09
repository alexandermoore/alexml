from Object import Object
from Constants import *
from ..AlexML.ReinforcementLearning import EGreedyQLearner

class Player(Object):
	def __init__(self, learner_class=EGreedyQLearner):
		super(Object, self).__init__()
		self.width = globalsize
		self.height = globalsize
		self.learner = learner_class()
		self.type = "player"