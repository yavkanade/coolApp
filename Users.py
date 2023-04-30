# users.py
import os
from User import User

class Users:
    def __init__(self):
        self.users = []
        self.user_data_folder = 'userData'

    def add_user(self, user):
        self.users.append(user)
        self.save_user(user)

    def save_user(self, user):
        if not os.path.exists(self.user_data_folder):
            os.makedirs(self.user_data_folder)

        user_file = os.path.join(self.user_data_folder, f'{user.email}.txt')
        with open(user_file, 'w') as f:
            f.write(f'{user.email}\n')
            f.write(f'{user.name}\n')
            f.write(f'{user.age}\n')
            f.write(f'{user.neighbourhood}\n')
            f.write(f'{user.points}\n')

    def authorize_user(self, email):
        user_file = os.path.join(self.user_data_folder, f'{email}.txt')
        if os.path.exists(user_file):
            with open(user_file, 'r') as f:
                email = f.readline().strip()
                name = f.readline().strip()
                age = f.readline().strip()
                neighbourhood = f.readline().strip()
                points = int(f.readline().strip())
                user = User(email, name, age, neighbourhood, points)
                return user
        else:
            return None
