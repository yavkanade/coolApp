import random
import os
from User import User
from Users import Users

class UserGenerator:
    def __init__(self):
        pass

    def generate_users(self, user_number):
        names = [
            "Emma", "Olivia", "Ava", "Isabella", "Sophia",
            "Charlotte", "Mia", "Amelia", "Harper", "Evelyn"
        ]
        
        last_names = [
            "Smith", "Johnson", "Williams", "Jones", "Brown",
            "Miller", "Davis", "Garcia", "Rodriguez", "Martinez"
        ]
        
        email_domains = [
            "@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com",
            "@mail.com", "@zoho.com", "@icloud.com", "@protonmail.com",
            "@me.com", "@yandex.com"
        ]
        
        phone_area_codes = [
            "403", "587", "780", "204"
        ]

        neighbourhoods = [
            "Central", "Uptown", "Downtown", "Midtown",
            "Northside", "Southside", "Westside", "Eastside",
            "Greenwood", "Brookfield"
        ]

        user_system = Users()

        for j in range(user_number):
            first_name = random.choice(names)
            last_name = random.choice(last_names)
            name = first_name + " " + last_name
            email = (first_name + last_name).lower() + str(j) + random.choice(email_domains)
            phone = random.choice(phone_area_codes) + str(random.randint(100, 999)) + str(random.randint(1000, 9999))
            age = random.randint(18, 65)
            neighbourhood = random.choice(neighbourhoods)
            password = "pass" + str(j)

            user = User(email, name, age, neighbourhood, password)
            user_system.save_user(user)

if __name__ == "__main__":
    generator = UserGenerator()
    generator.generate_users(10)  