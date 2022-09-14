class MuffledCalculator:
    muffled = False
    def calc(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.muffled:
                print('Division by zero is illegal')
            else:
                raise

calculator = MuffledCalculator()
try:
    calculator.calc('10/0')
except Exception as e:
    print('Tried division by zero: ', type(e))

calculator.muffled = True
calculator.calc('10/0')
