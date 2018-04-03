class Strategy:
    # _strategy = None

    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_operation(self):
        self._strategy.algorithm()


class ConcreteStrategy1:
    def algorithm(self):
        print("Execute algorithm of Strategy1")


class ConcreteStrategy2:
    def algorithm(self):
        print("Execute algorithm of Strategy2")


if __name__ == "__main__":
    context = Strategy(ConcreteStrategy1())
    context.execute_operation()
    context.set_strategy(ConcreteStrategy2())
    context.execute_operation()
