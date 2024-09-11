def sandwich(size, *toppings):
    print(f"\nThe sandwich's toppings are:", toppings, "size: ", size)
    # for a in toppings:
    #     print(f"- {a}")
    # return toppings


def user_profile(first,last,**user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info


def make_car(manufacturer, *stars):
    a = ''
    for star in stars:
        a = a + star + ','
        print(f"{star} are the {manufacturer} product.")
    return a[:-1]

def add1(a, b):
    c = a + b
    return c


