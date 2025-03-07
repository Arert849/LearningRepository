a_name = "Alice"
a_age = 7

b_name = "Dorothy"
b_age = 11

if a_age > b_age:
    print(f"{a_name} is older than {b_name}.")
elif a_age < b_age:
    print(f"{b_name} is older than {a_name}.")
else:
    print(f"{a_name} and {b_name} are the same age.")

bool_list = [True, True, False, True]

if all(bool_list):
    print("All values are True")    # Will not print

if any(bool_list):
    print("Some values are True")   # Will print

if not all(bool_list):
    print("Not all values are True")    # Will print due to the 'not' logical operator
