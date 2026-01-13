class agent:
    def __init__(self, name, age):
        print("welcome to the Game")
        self.name = name
        self.age = age
        self.health =100        # here Health would be a variable present for all objects as well
        self.isAlive = True
    
    def currentHealth(self):
        print("Current Health of", self.name, "is", self.health)
    def punched(self):
        self.health-=10
        self.checkAlive()
    def shooted(self):
        self.health-=50
        self.checkAlive()
    def checkAlive(self):
        if self.health>0:
            self.isAlive = True
            print(self.name,"is","Alive")
        else:
            self.isAlive = False
            print(self.name,"is","not Alive")
    def agentInfo(self):
        print("Agent name is    ",self.name)
        print("Agent age is    ",self.age)
        print("Agent health is    ",self.health)
        print("Agent is Alive   ",self.isAlive)

a1 = agent("Samm",30)
a1.punched()
a1.shooted()
a1.shooted()
a1.agentInfo()
print('*'*50)

a2 = agent("Samm",30)
a2.punched()
a2.shooted()
a2.agentInfo()
print('*'*50)

class boss(agent):                  # inheritance boss parent class is agent
    def power(self):
        print("Blow fire")

b1 = boss("Rishabh",29)             # here we need to define both arguments which are defined in  Super class
b1.agentInfo()
b1.power()

# Boss inherits from the Agent class, so it automatically has access to all methods 
# and attributes of Agent.
# The __init__ method of Agent initializes the 
# name, age, health, and alive attributes when a Boss object is created.
