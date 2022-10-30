"""
  --打印于谦的所有爱好(一行一个)
  --打印所有人(一行一个)
  --打印所有爱好(一行一个)
"""
dict_hobbies = {
    "于谦": ["抽烟", "喝酒", "烫头"],
    "郭德纲": ["说", "学", "逗", "唱"],
}

for item in dict_hobbies["于谦"]:
    print(item)

for key in dict_hobbies:
    print(key)

for value in dict_hobbies.values():
    for item in value:
        print(item)

# ----------------------------------------
# dict_hobbies["于谦"].remove("抽烟")
# del dict_hobbies["于谦"][0]
dict_hobbies["大爷"] = dict_hobbies["于谦"]
del dict_hobbies["于谦"]
print(dict_hobbies)