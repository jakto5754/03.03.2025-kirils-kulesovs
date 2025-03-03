import random

class Object:
    def __init__(self, type, DOC):
        self.type = type
        self.DOC = DOC

class Book(Object):
    def __init__(self, DOC, name, author):
        self.DOC = DOC
        self.name = name
        self.author = author

class Animal:
    def __init__(self, type, name, age):
        self.type = type
        self.name = name
        self.age = age

class BankasKonta:
    def __init__(self, bilance=0):
        self.bilance = bilance

    def depozits(self, summa):
        if summa > 0:
            self.bilance += summa
        else:
            raise ValueError("hgfhfghfghgfhfghgfhgf")
        
    def iznemums(self, summa):
        if summa > 0:
            self.bilance -= summa
        else:
            raise ValueError("hgfhfghfghgfhfghgfhgf")

print("\033[1m  MONEY  \033[0m")

g = random.randint(0, 1000)
account = BankasKonta(g)
randdep = random.randint(1, 500)
randwith = random.randint(1, 500)
print("Initia balance:", account.bilance)
account.depozits(randdep)
print("Depozit:", randdep)
account.iznemums(randwith)
print("Withdrawal:", randwith)
print("Bilance now:", account.bilance, "\n")

print("\033[1m  LITERATURE  \033[0m")


for _ in range(5):
    names = ["Hz ne pridumal", "Moby Dick", "Evil...", "The Bible", "Theory of Everything", "Darude Sandstorm"]
    authors = ["George Orwell", "Alexander Popov", "Gennady Gorin", "Dimitri Saran", "Kolobanov", "Suzanne Collins"]
    randdate = random.randint(100, 2025)
    randname = random.choice(names)
    randauthor = random.choice(authors)
    b = Book(randdate, randname, randauthor)
    print(b.DOC)
    print(b.name)
    print(b.author)
    print("\n")

print("\033[1m  ANIMALS  \033[0m")


for _ in range(5):
    types = ["Dog", "Cat", "Parrot", "Lama", "Opposum", "Opossum", "Sheep", "Cow", "Chicken", "Pig"]
    names2 = ["Gorin", "Opezdol", "Gavryusha", "Dostoevki"]
    randtype = random.choice(types)
    randname2 = random.choice(names2)
    randage = random.randint(1, 20)
    a = Animal(randtype, randname2, randage)
    print(a.type)
    print(a.name)
    print(a.age)
    print("\n")