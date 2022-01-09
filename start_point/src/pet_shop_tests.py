customers = [
    {
        "name": "Alice",
        "pets": [],
        "cash": 1000
    },
    {
        "name": "Bob",
        "pets": [],
        "cash": 50
    },
    {
        "name": "Jack",
        "pets": [],
        "cash": 100
    }
]

new_pet = {
        "name": "Bors the Younger",
        "pet_type": "cat",
        "breed": "Cornish Rex",
        "price": 100
    }

cc_pet_shop = {
    "pets": [
        {
            "name": "Sir Percy",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "King Bagdemagus",
            "pet_type": "cat",
            "breed": "British Shorthair",
            "price": 500
        },
        {
            "name": "Sir Lancelot",
            "pet_type": "dog",
            "breed": "Pomsky",
            "price": 1000,
        },
        {
            "name": "Arthur",
            "pet_type": "dog",
            "breed": "Husky",
            "price": 900,
        },
        {
            "name": "Tristan",
            "pet_type": "cat",
            "breed": "Basset Hound",
            "price": 800,
        },
        {
            "name": "Merlin",
            "pet_type": "cat",
            "breed": "Egyptian Mau",
            "price": 1500,
        }
    ],
    "admin": {
        "total_cash": 1000,
        "pets_sold": 0,
    },
    "name": "Camelot of Pets"
}

### FUNCTIONS ###

def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop, cash):
    pet_shop["admin"]["total_cash"] += cash


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop, pets_sold):
    pet_shop["admin"]["pets_sold"] += pets_sold

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    found = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            found.append(pet)

    return found


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet


def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, removed_cash):
    customer["cash"] -= removed_cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, pet):
    customer["pets"].append(pet)

def customer_can_afford_pet(customer, pet):
    if customer["cash"] >= pet["price"]:
        return True
    else:
        return False

def pet_exists(pet_shop, pet):
    if find_pet_by_name(pet_shop, pet) != None:
        return True
    else:
        return False


# def sell_pet_to_customer(pet_shop, pet, customer):
#     if find_pet_by_name(pet_shop, pet):
#         print("Pet Not Found")
#     else:
#         if customer_can_afford_pet(customer, pet):
#             add_pet_to_customer(customer, pet)
#             remove_customer_cash(customer, pet["price"])
#             remove_pet_by_name(pet_shop, pet)
#             add_or_remove_cash(pet_shop, pet["price"])
#             increase_pets_sold(pet_shop, 1)


# def sell_pet_to_customer(pet_shop, pet_name, customer):
#     if customer_can_afford_pet(customer, pet_name):
#                 add_pet_to_customer(customer, pet_name)
#                 remove_customer_cash(customer, pet_name["price"])
#                 remove_pet_by_name(pet_shop, pet_name)
#                 add_or_remove_cash(pet_shop, pet_name["price"])
#                 increase_pets_sold(pet_shop, 1)

# VERSION 9,876:

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is not None and customer_can_afford_pet(cc_pet_shop, pet):
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        remove_pet_by_name(pet_shop, pet)
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)
        

# DETAILS FOR TEST
#     customer = self.customers[0]
#     pet = find_pet_by_name(self.cc_pet_shop,"Arthur")

#     sell_pet_to_customer(self.cc_pet_shop, pet, customer)

#     self.assertEqual(1, get_customer_pet_count(customer))
#     self.assertEqual(1, get_pets_sold(self.cc_pet_shop))
#     self.assertEqual(100, get_customer_cash(customer))
#     self.assertEqual(1900, get_total_cash(self.cc_pet_shop))

pet_1 = find_pet_by_name(cc_pet_shop,"Arthur")
pet_2 = find_pet_by_name(cc_pet_shop,"Jimmy")

sell_pet_to_customer(cc_pet_shop, pet_1, customers[0])
print(get_customer_pet_count(customers[0]))
sell_pet_to_customer(cc_pet_shop, pet_2, customers[1])
print(get_customer_pet_count(customers[1]))
sell_pet_to_customer(cc_pet_shop, pet_1, customers[0])
print(get_customer_pet_count(customers[0]))



# sell_pet_to_customer(cc_pet_shop, pet_2, customers[0])
# print(get_customer_pet_count(customers[0]))

# print(find_pet_by_name(cc_pet_shop, "Billy"))
# print(find_pet_by_name(cc_pet_shop, "Arthur"))
# print(find_pet_by_name(cc_pet_shop, "Arthur") is None)
# print(find_pet_by_name(cc_pet_shop, "Billy") is None)


# x = None

# if x is None:
#     print("True")
# else:
#     print("False")

# print(pet_1)
# print(pet_2)

# print(pet_1 == None)
# print(pet_2 == None)

# print(pet_exists(cc_pet_shop, "Arthur"))
# print(pet_exists(cc_pet_shop, "Brad"))

# IT FINALLY WORKS. In the main file, anyway: For some reason I get KeyError: 'cash'
# running it in this file, but I'll try to puzzle that out at a later date.