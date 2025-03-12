# Pytest ---> Testing framework for python

# Unit test ---> smallest type of test
# Usually used for testing small components of code e.g:- functions etc.

import pytest

def addition(x,y):
    return x + y

def subtraction(x,y):
    return x - y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
    

def weather(temp):
    if temp > 25:
        return "Hot"
    elif temp < 15:
        return "Cold"
    else:
        return "Mild"


# Assert ---> tells us if something is true or false
# If True ---> test case passed else it failed
def test_add():
    assert addition(1,2) == 3

def test_sub():
    assert subtraction(2,1) == 1  

def test_divide():
    #assert divide(4,2) == 2
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(4,0) # Checking if the function raises the ValueError exception
    

def test_weather():
    assert weather(30) == "Hot"
    assert weather(10) == "Cold"
    assert weather(20) == "Mild"    
    





    

### Testing class ###
# Testing class with fixtures
class UserManager:
    def __init__(self):
        self.users = {}
    
    def add_users(self,username,email):
        if username in self.users:
            raise ValueError("Username already exists")
        self.users[username] = email
        return True
    def get_user(self,username):
        return self.users.get(username)
    def del_user(self,username):
        if username not in self.users:
            raise ValueError("Username does not exist")
        del self.users[username]
        return True
    

@pytest.fixture
def user_manager():
    "Creates fresh instance of the class before each test" # Doesn't want one test to interfere with another test due to same class used in multiple tests
    user_manager = UserManager()
    yield user_manager # Creating the fixture instance of the class
    user_manager.users.clear() # Clearing the instance after the test is done


def test_class(user_manager): # Fixtures are added as arguements in Test class
    
    user_manager.add_users("John","abc@gmail.com")
    with pytest.raises(ValueError,match="Username already exists"):
        user_manager.add_users("John","abc@gmail.com")
        
    user_manager.add_users("Alice","efg@gmail.com")

def test_del_func(user_manager):
    user_manager.add_users("John","abc@gmail.co,m")
    assert user_manager.del_user("John") == True
    
    with pytest.raises(ValueError,match="Username does not exist"):
        user_manager.del_user("Alice")               
                





### Parametrized testing ###

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

## Rather than mentioning each possible case in assert in the test function, we could mention the cases inside the 'mark parametrize' generator and pass it as an arguement in the test_function
## This is called parametrized testing. It is used to test the function with multiple test cases at once.


@pytest.mark.parametrize('num, expected',[
    (1,False),
    (2,True),
    (3,True),
    (4,False),
    (5,True),
    (6,False),
    (7,True),
    (8,False),
    (9,False),
    (10,False),
])

def test_prime(num,expected):
    assert is_prime(num) == expected  