# TC: O(1) SC: O(1)
def get_first_item(items):
    return items[0]


# TC: O(N) SC: O(1)
def print_all_items(items):
    for item in items:
        print(item)


# The Quadratic Time Trap
# Loop inside a loop
# TC: O(N^2) SC: O(1)
def print_pairs(items):
    for i in items:                     # TC: O(N)
        for j in items:                 # TC: O(N)
            print(i, j)


# SC: O(N)
def create_doubles(items):
    doubled_items = []
    for item in items:
        # SC: O(N) as new list will be created with same count of digits as input
        doubled_items.append(item*2)
    return doubled_items
