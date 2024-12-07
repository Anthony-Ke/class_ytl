import pandas as pd
import random


building_names = [i for i in range(1,5)]
block_names = [i for i in range(1,3)]
floors = [i for i in range(1,9)]
rooms = [i for i in range(1,5)]
genders = ["male", "female"]
ages = ["infant", "child", "teenager", "adult", "middle_aged", "senior"]

def generate_room_number(seed):
    random.seed(seed)
    building = random.choice(building_names)
    block = random.choice(block_names)
    floor = random.choice(floors)
    room = random.choice(rooms)
    return f"{building}栋{block}单元{floor}0{room}"

address_list = [generate_room_number(i) for i in range(1500)]
ages_list = [random.choice(ages) for i in range(1500)]
genders_list = [random.choice(genders) for i in range(1500)]

df = pd.DataFrame({"address": address_list, "age": ages_list, "gender": genders_list})
df.to_csv("./population.csv", index=False)





