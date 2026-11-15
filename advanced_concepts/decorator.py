# decorator in python

def logger(func):
    def wrapper():
        print("Function is being called")
        func()
        print("Function has been called")
    return wrapper
@logger
def hello():
    print("Hello!")
hello()