import random


class Item:
    """Class for storage and creation of items."""

    def __init__(self,
                 name,
                 armor,
                 attack,
                 health) -> None:
        self.name = name
        self.armor = armor
        self.attack = attack
        self.health = health

    def generate(name: str):
        return Item(name, random.randint(1, 10) / 100, random.randint(10, 30), random.randint(100, 200))


class Person:
    """Basic class for characters."""

    def __init__(self, name="name",
                 health: int = 100,
                 attack: int = 10,
                 armor: float = 0.1) -> None:
        self.name = name
        self.health = health
        self.attack = attack
        self.armor = armor
        self.items = []

    def wear_item(self, item_list, item_num):
        while len(self.items) < item_num:
            item = random.choice(item_list)
            self.health += item.health
            self.attack += item.attack
            self.armor += item.armor
            if item.name not in self.items:
                self.items.append(item.name)
                print(f"{self.name} gets {item.name}")

    def get_damage(self, someone):
        damage = someone.attack - (self.armor * someone.attack)
        self.health = self.health - damage
        return f"{self.name} recieves damage {damage:.1f} from {someone.name}, his health: {self.health:.1f}"

    def generate(self):
        return Person(name, random.randint(100, 200), random.randint(10, 30), random.randint(1, 10) / 100)


class Paladin(Person):
    """Paladin with increased health."""

    def __init__(self,
                 name: str,
                 health: int,
                 attack: int,
                 armor: float,
                 ) -> None:
        super().__init__(name, health, attack, armor)
        self.health = health * 2

    def generate(self):
        return Paladin(name, random.randint(100, 200), random.randint(10, 30), random.randint(1, 10) / 100)


class Warrior(Person):
    """Warrior with increased attack."""

    def __init__(self,
                 name: str,
                 health: int,
                 attack: int,
                 armor: float,
                 ) -> None:
        super().__init__(name, health, attack, armor)
        self.armor = armor * 2

    def generate(self):
        return Warrior(name, random.randint(100, 200), random.randint(10, 30), random.randint(1, 10) / 100)


# Predefined arrays of names:

item_names = (["ring", "helmet", "sword", "gloves", "shield", "gem",
               "stone of soul", "bracers", "magic ward", "orb"])
char_names_paladins = ["frodo", "sam", "gendalf", "master", ]
char_names_warriors = ["terminator", "Bilbo", "Luk", "Arnold"]


def fight(fighter_1, fighter_2):
    """Return loser fighter."""
    while True:
        print(fighter_1.get_damage(fighter_2))
        if fighter_1.health < 0:
            print(f"{fighter_1.name} умирает")
            return fighter_1
            break
        print(fighter_2.get_damage(fighter_1))
        if fighter_2.health < 0:
            print(f"{fighter_2.name} умирает")
            return fighter_2
            break


# Create items with random parameters:
generated_items = []
for name in item_names:
    generated_items.append(Item.generate(name))
# Create fighters with random parameters:
generated_persons = []
for name in char_names_paladins:
    generated_persons.append(Paladin.generate(name))
for name in char_names_warriors:
    generated_persons.append(Warrior.generate(name))
# Equip fighters with generated items:
for person in generated_persons:
    person.wear_item(generated_items, random.randint(1, 4))

# Start the fight:
while len(generated_persons) > 1:
    # Randomly choose two fighters from the list:
    fighter1 = 0
    fighter2 = 0
    while fighter1 == fighter2:
        fighter1 = random.choice(generated_persons)
        fighter2 = random.choice(generated_persons)
    # Perform the fight ant remove loser from the array:
    generated_persons.remove(fight(fighter1, fighter2))
    print("Still alive:")
    for i in generated_persons:
        print(i.name)
print(f"Winner is {generated_persons[0].name}, class:{generated_persons[0].__class__.__name__}")
