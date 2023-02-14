import random


garden = ["покрышка", "бутылка", "окурок", "железяка", "череп коровы"]
garden.clear()
order = (
    ("ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис", "ирис"),
    ("роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза", "роза"),
    ("пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион", "пион")
)
for package in order:
  for seed in package:
    garden.append(seed)
weeds = ("борщевик", "крапива", "лопух")
for weed in weeds:
  for i in range(random.randint(5, 10)):
    garden.append(weed)
random.shuffle(garden)
print("сад до прополки:", garden)
print("\nидентификатор сада до прополки:", id(garden))

def weeding(garden: list, weeds: tuple) -> None:
    for i in range(len(garden)):
        for n in range(len(weeds)):
            if garden[i] == weeds[n]:
                garden.pop(i)
                return weeding(garden, weeds)


weeding(garden, weeds)

print("\nсад после прополки:", garden)
print("\nидентификатор сада после прополки:", id(garden))

flowers_quantity = len(garden)
print(f"\nобщее количество цветов: {flowers_quantity}")

bouquet = random.sample(garden, 5)

print(f"\nбукет: {bouquet}")
    
