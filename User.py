# user.py
class User:
    def __init__(self, email, name, age, neighbourhood, points=0):
        self.email = email
        self.name = name
        self.age = age
        self.neighbourhood = neighbourhood
        self.points = points

        self.items = []
        self.events = []

    # Setters
    def set_email(self, email):
        self.email = email

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_neighbourhood(self, neighbourhood):
        self.neighbourhood = neighbourhood

    def set_points(self, points):
        self.points = points

    # Getters
    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_neighbourhood(self):
        return self.neighbourhood

    def get_points(self):
        return self.points
