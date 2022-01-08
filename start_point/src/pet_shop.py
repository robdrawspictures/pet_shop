# WRITE YOUR FUNCTIONS HERE
pet_shop_1 = {
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


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]
        # return item

print(get_pet_shop_name(pet_shop_1))

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

# def sell_pet_to_customer(pet_shop, pet, customer):
#     if customer_can_afford_pet(customer, pet):
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         add_or_remove_cash(pet_shop, pet["price"])
#         get_total_cash(pet_shop)
#         increase_pets_sold(pet_shop, 1)
#         get_pets_sold(pet_shop)

# ^ Backup working for No.21 (and No.23, I think)

def sell_pet_to_customer(pet_shop, pet, customer):
    if find_pet_by_name(pet_shop, pet) is None:
        get_customer_pet_count(customer)
        get_pets_sold(pet_shop)
        get_customer_cash(customer)
        get_total_cash(pet_shop)
    else:
        if customer_can_afford_pet(customer, pet):
            add_pet_to_customer(customer, pet)
            remove_customer_cash(customer, pet["price"])
            remove_pet_by_name(pet_shop, pet)
            add_or_remove_cash(pet_shop, pet["price"])
            increase_pets_sold(pet_shop, 1)

            
    
# def sell_pet_to_customer(pet_shop, pet, customer):
#     if customer_can_afford_pet(customer, pet):
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         add_or_remove_cash(pet_shop, pet["price"])
#         increase_pets_sold(pet_shop, 1)

    