from environment import Agent

class LearningAgent(Agent):
	def __init__(self, env):
        self.env = env
        self.color = 'white'
        self.primary_agent = True
    def reset(self, destination=None, testing=False):
    	if 
