class User:
    def __init__(self,id, name):
        print("hello")
        self.user_id=id
        self.user_name=name
        self.followers=0
        self.following=0

    def follow(self,user):
        self.followers+=1
        user.following+=1
        
# user =User()
# user.name="Pravin"
# user.id="001"

# user1 =User()
# user1.username="Yadu"
# user1.id="002"

# print(user1.username)
# print(user1.id)

user=User("001","Pravin")
user2=User("002","Yadu")
user2.follow(user)
print(user.user_id)
print(user.user_name)    
print(user.followers)  
print(user.following)   
print(user2.user_id)
print(user2.user_name)
print(user2.followers)   
print(user2.following)   
  
