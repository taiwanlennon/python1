class Superclass:
    def __init__(self):
        print("Superclass")
    def supermethod(self):
        print("supermethod")
class Subclass(Superclass):
    def __init__(self):
        print("Subclass")

    def submethod(self):
        print("submethod")

demo = Subclass()
demo.submethod()
