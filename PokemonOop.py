class Pokemon:
    pass

    def __int__(self, name, typePokemon):
        self.name = name
        self.type = typePokemon

    def description(self):
        return print(f"{self.name} is {self.type}")

    def attack(self, attackName):
        return print(f"{self.name} is attacking with {attackName}")


pikachu = Pokemon()
pikachu.__int__("Pikachu", "Electric")
pikachu.description()
pikachu.attack("Ray")
