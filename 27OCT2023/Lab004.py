# Nested tuples -> Tuple within tuple

hero1 = ("Bruce Wayne", "Batman")
hero2 = ("Clark Kent", "Superman")
merge_hero = (hero1, hero2)
print(merge_hero)

print(merge_hero[0])
print(merge_hero[0][1])
print(merge_hero[1])
print(merge_hero[1][0])
