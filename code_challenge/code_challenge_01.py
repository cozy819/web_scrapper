days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def is_on_list(days, day):
    return day in days


print("Is Wed on 'days' list?", is_on_list(days, "Wed"))


def get_x(days, order):
    return days[order]


print("The fourth item in 'days' is:", get_x(days, 3))


def add_x(days, day):
    days.append(day)


add_x(days, "Sat")
print(days)


def remove_x(days, day):
    days.remove(day)


remove_x(days, "Mon")
print(days)
