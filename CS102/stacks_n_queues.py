from collections import deque

alice_backpack = ["potion", "key"]
bob_backpack = ["shield"]
cara_backpack = ["scroll", "dagger"]

door_queue = deque([
    ("Alice", alice_backpack),
    ("Bob", bob_backpack),
    ("Cara", cara_backpack),
])

print("Full queue:", door_queue)

while door_queue:
    name, backpack = door_queue.popleft()
    print("\nNow entering:", name)

    if backpack:  # they have at least one item
        used_item = backpack.pop()
        print("Item used:", used_item)
        print("Backpack after:", backpack)
    else:
        print("No items left in backpack!")
