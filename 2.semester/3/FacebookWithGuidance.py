class User:
    def __init__(self,name):
        self.name = name
        self.friends = []# store objects of type user whom are your friends
        self.requests=[]
        self.outrequests = []
        self.wall = Wall(self)

    def addFriend(self,person):#takes a user as a parameter
        friendrequest = Request(self,person)
        person.addFriendReq(friendrequest)
        self.outrequests.append(friendrequest)
    def addFriendReq(self,request):
        self.requests.append(request)
    def approve(self,request):
        #here we get the request object
        self.friends.append(request.sender)
        request.sender.friends.append(self)
        #I add both of the people in eachothers friend lists
        #and remove them from eachothers requests
        self.requests.pop(self.requests.index(request))
        request.sender.outrequests.pop(request.sender.outrequests.index(request))
    def post(self,content):
        post = Post(self,content)
        self.wall.addContent(post)
        print(f"{self} just posted '{post}'")
        for friend in self.friends:
            friend.wall.addOtherContent(post)
    def __repr__(self):
        return self.name
class Post:
    def __init__(self,originalPoster,Content):
        self.originalPoster = originalPoster
        self.Content = Content
    def __repr__(self):
        return self.Content
class Wall:
    def __init__(self,owner):
        self.owner = owner
        self.content = []
    def addContent(self,post):
        self.content.append(post.Content)
    def addOtherContent(self,post):
        self.content.append(f'[{post.originalPoster}] {post.Content}')
    def __repr__(self):
        bs = ""
        bs+= f'Wall:{self.owner}\n================\n'
        for element in self.content:
            bs = bs+element+"\n"

        return bs
class Request:
    def __init__(self,sender,reciever):
        self.sender = sender #A user object
        self.reciever = reciever #also a user object
    def __repr__(self):
        return "Add friend request from "+self.sender.name

u1 = User ("Joe")
u2 = User ("Jill")
print (u1.name + " Friend List = " + str(u1.friends))
u1.addFriend(u2)
print (u2.name + " Friend Requests = " + str(u2.requests))
u2.approve (u2.requests[0])
print (u1.name + " Friend List = " + str(u1.friends))


p1 = u1.post("What a lovely weekend")
print (u2.wall)
p2 = u2.post("Sunny and warm!")
print(u2.wall)