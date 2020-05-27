# -*- coding: utf-8 -*-

# 字典
# 创建字典
alien_0 = {}
alien_0 = {"color": "green", "points": 5, "name": "green"}

# 读取
print(alien_0["color"])
# KeyError: "age"
# print(alien_0["age"])

# 添加
alien_0["age"] = 12
print(alien_0)

# 修改
alien_0["age"] = 111
print(alien_0)

# 删除
del alien_0["points"]
print(alien_0)

# 遍历(默认是 keys)
print("===========")

for key, value in alien_0.items():
    print("key: ", key, ", value: ", value)

print("===========")

for key in alien_0.keys():
    print("key: ", key)

print("===========")

for value in alien_0.values():
    print("value: ", value)

print("===========")
# 排序遍历
for key in sorted(alien_0):
    print("kk: ", key)

print("===========")
# 去重 set()
for value in set(alien_0.values()):
    print("set-value: ", value)

print("===========")
# 嵌套（字典存入列表/列表存入字典）
alien_11 = {"color": "green", "points": 5}
alien_12 = {"color": "yellow", "points": 10}
alien_13 = {"color": "red", "points": 15}
aliens = [alien_11, alien_12, alien_13]

for alien in aliens:
    print(alien)

print("===========")
# test 1
aliensGroup = []
for alien_num in range(30):
    new_alien = {
        "color": "greed",
        "points": 5,
        "speed": "slow"
    }
    aliensGroup.append(new_alien)
# print(aliensGroup)
for alien in aliensGroup[10:20]:
    alien["color"] = "yellow"
    alien["points"] = 10
    alien["speed"] = "medium"

for alien in aliensGroup[20:]:
    alien["color"] = "red"
    alien["points"] = 15
    alien["speed"] = "fast"

for item in aliensGroup:
    print("new alien ", item)

# teat 2
favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"]
}
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:" + languages[0])
        print("\t" + languages[0].title())
    else:
        print("\n" + name.title() + "'s favorite language are:")
        for language in languages:
            print("\t" + language.title())
