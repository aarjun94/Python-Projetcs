
import random
from tokenize import group
import matplotlib.pyplot as plt
from IPython import display
import time

random.seed(32)



class Agent():
    def __init__(self, xlocation, ylocation):
        self.x = xlocation
        self.y = ylocation

agent1 = Agent(22, 55)
agent2 = Agent(66, 88)

def map_all_agents(listofagents):
    agents_XCoordinate = [] 
    agents_YCoordinate = [] 
    
    for item in listofagents:
      agents_XCoordinate.append(item.x)
      agents_YCoordinate.append(item.y)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(agents_XCoordinate, agents_YCoordinate, 'o', markerfacecolor='purple')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()

agents_list = [agent1, agent2]

def moveagents(listofagents):
    for each_agent in listofagents:
        each_agent.x = random.randint(0,100),
        each_agent.y = random.randint(0,100)
    return listofagents

def make_agents_dance(agentslist, num_steps=10):
    for i in range(num_steps):
      moveagents(agentslist)
      map_all_agents(agentslist)
      time.sleep(1)
      display.clear_output(wait=True)

New_List_of_Agents = [Agent(random.randint(0,100), random.randint(0,100)) for i in range(12)]

class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status="unhappy"):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status 




# The class AgentNew randomly picks whether an agent will be purple or gold.
# We may want to specify that instead, so lets create two subclasses of AgentNew.
# Let's call them PurpleAgents and GoldAgents.

class PurpleAgents(AgentNew):
        def __init__(self, xlocation, ylocation, group="Purple", status="unhappy"):
            super().__init__(xlocation, ylocation, group)
            self.group = group
            self.status = status

b1 = PurpleAgents(3,6)
print(b1.group)

class GoldAgents(AgentNew):
        def __init__(self, xlocation, ylocation, group="Gold", status="unhappy"):
            super().__init__(xlocation, ylocation, group)
            self.group = group
            self.status = status

b2 = GoldAgents(3,6)
print(b2.group)


random.seed(15)
List_of_PurpleAgents = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for x in range(12)]  ### using list comprehension, make 12 PurpleAgents
List_of_GoldAgents = [GoldAgents(random.randint(0,100), random.randint(0,100)) for x in range(12)] ### using list comprehension, make 12 GoldAgents
Combined_List = List_of_PurpleAgents + List_of_GoldAgents 

def map_colorful_agents(CombinedList):  # what argument should go in this function?

    Purple_XCoordinate = [CombinedList[i].x for i in range(len(CombinedList)) if CombinedList[i].group =="Purple"] ### fill in the blanks to make this list comprehension work
    Purple_YCoordinate = [CombinedList[i].y for i in range(len(CombinedList)) if CombinedList[i].group =="Purple"] # model this after the above list comprehension
    Gold_XCoordinate = [CombinedList[i].x for i in range(len(CombinedList)) if CombinedList[i].group =="Gold"]
    Gold_YCoordinate = [CombinedList[i].y for i in range(len(CombinedList)) if CombinedList[i].group =="Gold"]

    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('azure')
    ax.plot(Purple_XCoordinate, Purple_YCoordinate, 'o', markerfacecolor='purple')
    ax.plot(Gold_XCoordinate, Gold_YCoordinate, 'o', markerfacecolor='gold')
    plt.xlim(-5,105)
    plt.ylim(-5,105)
    ax.set_title("Here's our map of the agents we have created:")
    plt.show()

x = map_colorful_agents(Combined_List)
### call the function appropriately



# Now that we have some agents of different groups

random.seed(38)
class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status='unhappy'):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status

    def move_if_unhappy (self):  # what arguement(s) are needed here?
        if self.status == "unhappy":  ### there is a mistake in this command - fix it
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

a55 = AgentNew(24,11,"Purple")



'''Problem #4'''

# Now we are going to make our most complicated method.
# We're going to build a method called 'check_neighbors' which will identify
# the agents that are within 10 x-coordinate AND 10 y-coordinate spaces of a
# given agent. Once those agents are identified, we'll calculate if enough of
# them are of the same group to meet our pre-determined threshold.

class AgentNew(Agent):
    def __init__(self, xlocation, ylocation, group, status='unhappy'):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status


    def move_if_unhappy (self):
        if self.status == "unhappy":
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

    def check_neighbors(self, agentlist): 
        zlist = list(filter(lambda t: abs(t.x - self.x) <10, agentlist))
        zlist = list(filter(lambda t: abs(t.y - self.y) <10, zlist))
        same_group_neighbor = [t for t in zlist if t.group == self.group]
        opposite_group_neighbor = [t for t in zlist if t.group != self.group] 
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold:
            self.status="happy"
        else:
            self.status="unhappy"


class PurpleAgents(AgentNew):
        def __init__(self, xlocation, ylocation, group="Purple"):
            super().__init__(xlocation, ylocation, group, status='unhappy')
            self.group = group

          

        def move_if_unhappy(self):
            return super().move_if_unhappy()

        def check_neighbors(self, agentlist):
            return super().check_neighbors(agentlist)

class GoldAgents(AgentNew):
        def __init__(self, xlocation, ylocation, group="Gold"):
            super().__init__(xlocation, ylocation, group, status='unhappy')
            self.group = group
     
        def move_if_unhappy(self):
            return super().move_if_unhappy()
            
        def check_neighbors(self, agentlist):
            return super().check_neighbors(agentlist)



random.seed(34)
p32 = PurpleAgents(14,55)
p32.move_if_unhappy()
print(p32.x)  # what do you expect the output to be?



# Now we're ready to put it all together and run a few simulations.
# First, let's run a simulation in which there are 200 Purple agents and
# 200 Gold agents.
# Notice the group_affinity_threshold is set at .51.
# This means each purple or gold agent wants to be in a 'block' in which they
# are in the majority group.

random.seed(2021)
group_affinity_threshold = .51
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for x in range(200)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for x in range(200)]

map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist)  # does this need any arguments?
    for agent in (testlist):
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)



random.seed(202)
group_affinity_threshold = .4
testlist = [PurpleAgents(random.randint(0,100), random.randint(0,100)) for x in range(400)] + [GoldAgents(random.randint(0,100), random.randint(0,100)) for x in range(400)] ### create a testlist that has 200 PurpleAgents and 200 GoldAgents###### create a testlist that has 400 PurpleAgents and 400 GoldAgents
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist)  #does this need any arguments?
    for agent in (testlist):
        agent.move_if_unhappy() # does this need any arguments?
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)

'''Problem #7'''

# Even if people don't mind being a minority in their neighborhood, you still
# get segregation pretty easily according to this model. For a long time models
# such as this were used to argue that some degree of segregation was
# inevitable, and therefore it should not be a target of policy.


# Lets make 2 new subclasses, 'PurpleDiversitySeekers' and 'GoldDiversitySeekers'.
# Please use those exact names to allow for autograding.
# For these subclasses, make them seek out diversity instead of avoid it.
# Run some simulations with 300 traditional PurpleAgents, 300 traditional
# GoldAgents, 100 PurpleDiversitySeekers, and 100 GoldDiversitySeekers.
# What happens now?

random.seed(11)

class PurpleDiversitySeekers(Agent):
    def __init__(self, xlocation, ylocation, group='Purple', status='unhappy'):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status


    def move_if_unhappy (self):
        if self.status == "unhappy": 
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

    def check_neighbors(self, agentlist): 
        zlist = list(filter(lambda x: abs(x.x - self.x) <10, agentlist))
        zlist = list(filter(lambda x: abs(x.y - self.y) <10, zlist))
        same_group_neighbor = [t for t in zlist if t.group != self.group]
        opposite_group_neighbor = [t for t in zlist if t.group == self.group] 
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: 
            self.status="happy"
        else:
            self.status="unhappy"

class GoldDiversitySeekers(Agent):
    def __init__(self, xlocation, ylocation, group='Gold', status='unhappy'):
        super().__init__(xlocation, ylocation)
        self.group = group
        self.status = status


    def move_if_unhappy (self):
        if self.status == "unhappy": 
            self.x = random.randint(0,100)
            self.y = random.randint(0,100)

    def check_neighbors(self, agentlist):  
        zlist = list(filter(lambda x: abs(x.x - self.x) <10, agentlist))
        zlist = list(filter(lambda x: abs(x.y - self.y) <10, zlist))
        same_group_neighbor = [t for t in zlist if t.group != self.group]
        opposite_group_neighbor = [t for t in zlist if t.group == self.group] 
       
        if (len(same_group_neighbor)+.01)/(len(zlist)+.01) > group_affinity_threshold: 
            self.status="happy"
        else:
            self.status="unhappy"

group_affinity_threshold = .51
testlist = [AgentNew(random.randint(0,100), random.randint(0,100), group='Purple') for x in range(300)] + [AgentNew(random.randint(0,100), random.randint(0,100),  group='Gold') for x in range(300)] + [PurpleDiversitySeekers(random.randint(0,100), random.randint(0,100)) for x in range(100)] + [GoldDiversitySeekers(random.randint(0,100), random.randint(0,100)) for x in range(100)]
map_colorful_agents(testlist)
for x in range(15):
    for agent in (testlist):
        agent.check_neighbors(testlist) 
    for agent in (testlist):
        agent.move_if_unhappy() 
    map_colorful_agents(testlist)
    print(x)
    time.sleep(.5)
    display.clear_output(wait=True)


