import random
import json


# res = random.sample(range(1, 11565), 1157)
# dev_set = set(res)

# with open("data/train.txt", "r") as former_train:
#     train_out = open("data/new_train.txt", "w")
#     dev_out = open("data/dev.txt", "w")
#     for index, line in enumerate(former_train.readlines()):
#         if index + 1 in dev_set:
#             dev_out.write(line)
#         else:
#             train_out.write(line)
#     train_out.close()
#     dev_out.close()

with open("data/new_train_middle.json", "r") as f:
    dic = json.load(f)

print(dic["quo_list"])
