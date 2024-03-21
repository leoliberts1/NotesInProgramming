#I need the user with their name, email, friends list, friends req list, ability to add, reject friends
class User():
    def __init__(self,name):
        self.name = name
        self.outrequests = []
        self.requests = []
        self.friends = []
    def addFriend(self,Person):
        self.outrequests.append(Person)
        Person.requests.append(self)
    def approve(self,personInReq):
        self.friends.append(personInReq.name)
        #print(personInReq)
        self.requests.pop(self.requests.index(personInReq))
        #print(personInReq.outrequests)
        personInReq.outrequests.pop(personInReq.outrequests.index(self))
        personInReq.friends.append(self)
    def disaprove(self,personInReq):
        personInReq.outrequests.pop(self)
        self.requests.pop(personInReq)
    def __str__(self):return self.name
    def __repr__(self): return self.name
class Request():
    def __init__(self,sender,reciever):
        self.sender = sender
        self.reciever = reciever
        self.acceptance = False

u1 = User ("Joe")
u2 = User ("Jill")
print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print (u2.name + " Friend Requests = " + str(u2.requests))
u2.approve (u2.requests[0])
print (u1.name + " Friend List = " + str(u1.friends))