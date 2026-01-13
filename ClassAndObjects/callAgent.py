# Modules are simply python code having functions, classes, variables. 
# Any python file with .py extension can be referenced as a module.

import Agent

print(dir(Agent))       # it will return all the functions written in that class

agent_1 = Agent.agent("Mario",32)   # here "Agent" is name of the Module and "agent" is name of the class

print(dir(agent_1))     # it will return all the methods available for "agent_1"

a1 = Agent.agent("Shaktiman",32)
a1.health *=100         # we can assign values disrectly
a1.agentInfo()
print('*'*50)

a2 = Agent.agent("GangaDhar",32)
a2.agentInfo()
print('*'*50)


boss1 = Agent.boss("Kilvish",300)
a1.health *=1000
boss1.agentInfo()
print('*'*50)
