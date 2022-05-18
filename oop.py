

class user:
    def default(self):
        self.name="Osvaldo"
        self.sex="M"
        self.age=25

u = user()
u.default()
print(f"The name of the user is {u.name} and is {u.age} years old");