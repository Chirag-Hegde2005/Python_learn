#static and class methods

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")

result = MathUtils.add(5, 3)
print("Sum:", result)

MathUtils.description()