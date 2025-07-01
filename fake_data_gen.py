from faker import Faker
import random
from db import add_member, create_table

# Initialize faker and ensure table exists
faker = Faker()
create_table()

genders = ['Male', 'Female', 'Non-Binary']

for _ in range(15):
    firstname = faker.first_name()
    lastname = faker.last_name()
    gender = random.choice(genders)
    age = str(random.randint(18, 80))
    address = faker.address().replace("\n", ", ")
    contact = faker.msisdn()[0:10]  # Use 10-digit mobile-like number

    add_member(firstname, lastname, gender, age, address, contact)

print("✅ 15 random contacts inserted successfully.")
