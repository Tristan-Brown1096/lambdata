class BareMinimumClass:
    pass

class Complex:
    def __init__(self, realpart, imagpart):
        """Constructor for Complex numbers.
        Complex numbers are part real, part imaginary.
        Imaginary numbers are roots of negative numbers.
        """
        self.r = realpart
        self.i = imagpart

    def add(self, other_complex):
        self.r += other_complex.r
        self.i += other_complex.i

    def __repr__(self):
        return '({} + {}i)'.format(self.r, self.i)


class SocialMediaUser:
    def __init__(self, name, location, upvotes=0):
        self.name = str(name)
        self.location = location
        self.upvotes = int(upvotes)

    def receive_upvote(self):
        self.upvotes += 1

    def is_popular(self):
        return self.upvotes > 100


class Animal:
    """General representation of animals."""
    def __init__(self, name, weight, diet_type):
        self.name = str(name)
        self.weight = float(weight)
        self.diet_type = diet_type

    def run(self):
        return 'Vroom!'

    def eat(self, food):
        return food + ' is delicious, yum!'


class Tiger(Animal):
    def __init__(self, name, weight, diet_type, num_stripes):
        super().__init__(name, weight, diet_type)
        self.num_stripes = int(num_stripes)

    def say_great(self):
        return "It's GREEAAAAT"

    def run(self):
        return 'Scamperwoosh!'


if __name__ == '__main__':
    # Demo code if you run 'python oop_examples.py'
    # Example 0
    b = BareMinimumClass()
    # Example 1
    num1 = Complex(3, -5)
    num2 = Complex(-1, 6)
    num1.add(num2)
    print(num1)
    # Example 2
    user = SocialMediaUser("John Doe", "Anytown, USA")
    print(user.is_popular())
    for _ in range(125):
        user.receive_upvote()
    print(user.is_popular())
