phone_book = {"Batman": 876567,
              "Superman": 346567,
              "Flash": 876537}

print(phone_book)
print(len(phone_book))

print(phone_book["Batman"])
print(phone_book["Flash"])

pixar = dict(Cars=3, Toy_Story=4, Incredibles=2)
print(pixar)

print(pixar["Cars"])
print(pixar['Toy_Story'])
print(pixar.get("Incredibles"))

new_dict = dict(Name='Rocky', age=28, height=5.11, isMale=True)
print(new_dict)

new_dict2 = {1: 2, 3: 4, 5: 6, 7: 8}
print(new_dict2)
print(new_dict2[1])
print(new_dict2[3])
print(new_dict2[5])

print(new_dict2.keys())
print(new_dict2.values())
print(new_dict2.items())
