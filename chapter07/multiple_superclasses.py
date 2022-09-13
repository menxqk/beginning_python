class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talker:
    def talk(self):
        print('Hi, my value is', self.value)


class TakingCalculator(Calculator, Talker):
    pass


tc = TakingCalculator()
tc.calculate('1 + 2 * 3')
tc.talk()
