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

# def sell_pet_to_customer(pet_shop, pet, customer):
#     if customer_can_afford_pet(customer, pet):
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         add_or_remove_cash(pet_shop, pet["price"])
#         get_total_cash(pet_shop)
#         increase_pets_sold(pet_shop, 1)
#         get_pets_sold(pet_shop)

# ^ Backup working for No.21 (and No.23, I think)

# def sell_pet_to_customer(pet_shop, pet, customer):
#     if find_pet_by_name(pet_shop, pet) is None:
#         get_customer_pet_count(customer)
#         get_pets_sold(pet_shop)
#         get_customer_cash(customer)
#         get_total_cash(pet_shop)
#     else:
#         if customer_can_afford_pet(customer, pet):
#             add_pet_to_customer(customer, pet)
#             remove_customer_cash(customer, pet["price"])
#             remove_pet_by_name(pet_shop, pet)
#             add_or_remove_cash(pet_shop, pet["price"])
#             increase_pets_sold(pet_shop, 1)


# ^ Passes test No.22 and No.23 but not No.21, although
# I think No.23 is only passing for the same reason
# No.21 isn't: The block of code in the else condition
# isn't running.

# The error being returned is AssertionError 1 != 0, but
# I know the code in else definitely adds the pet properly
# because the test passes when I run it in isolation, so
# I can only assume putting it in else is creating
# a conflict, somehow.

# I think No.23 only passes because all the 
# assertEqual tests are expecting the info in the data
# set to stay the same since no pet is sold, so whether
# or not the code runs the result is the same.
             
# def sell_pet_to_customer(pet_shop, pet, customer):
#     if customer_can_afford_pet(customer, pet):
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         remove_pet_by_name(pet_shop, pet)
#         add_or_remove_cash(pet_shop, pet["price"])
#         increase_pets_sold(pet_shop, 1)

# Tidier version of the original function that passes
# No.21/23. I removed functions that didn't need to be
# included because the test calls them, itself.

# def sell_pet_to_customer(pet_shop, pet, customer):
#     if find_pet_by_name(pet_shop, pet) is None:
#         return None
#     else:
#         if customer_can_afford_pet(customer, pet):
#             add_pet_to_customer(customer, pet)
#             remove_customer_cash(customer, pet["price"])
#             remove_pet_by_name(pet_shop, pet)
#             add_or_remove_cash(pet_shop, pet["price"])
#             increase_pets_sold(pet_shop, 1)


### ATTEMPT NO.5,763: THE ONE THAT FINALLY WORKS ###

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet is not None and customer_can_afford_pet(customer, pet):
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        remove_pet_by_name(pet_shop, pet)
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)

# I am embarrassed to admit it took me 3 days to realise
# all my problems were because I was attempting to pass
# find_pet_by_name as an argument to find_pet_by_name.