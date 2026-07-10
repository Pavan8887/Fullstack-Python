def login(func):
    def wrapper():
        print("Checking login")
        func()
    return wrapper
@login

def dashboard():
    print("Dashboard page ")
dashboard()