class Calculator:
    calculation_type = "Arithmetic Operations"
    @staticmethod
    def add(a,b):
        return a+b

   

    @classmethod
    def multiply(cls,x, y):
        print(f"Calculation type: {cls.calculation_type}")
        return x * y

    