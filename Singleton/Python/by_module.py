import threading
import random
import time


class Generator(threading.Thread):

    def __init__(self, *args, **kwargs):
        threading.Thread(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.daemon = True

    def run(self):
        import settings
        writes = 0
        while writes < 100:
            with settings.generator_lock:
                if len(settings.list_as_singleton) < 20:
                    settings.list_as_singleton.append(random.random())
                    writes = writes + 1
            time.sleep(random.random() / 10000)
        print(f"Generator {self.getName()} finished.")


class Operator(threading.Thread):
    def __init__(self, *args, **kwargs):
        threading.Thread(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.daemon = True

    def run(self):
        import settings
        while True:
            with settings.operator_lock:
                if len(settings.list_as_singleton) > 0:
                    print(f"{settings.shared_counter}: {self.getName()}:\t{settings.list_as_singleton.pop()}")
                    settings.shared_counter += 1
            time.sleep(random.random() / 10)


if __name__ == "__main__":
    import settings

    if settings.generator_lock is settings.generator_lock:
        print("The same.")

    # start threads
    generators = []
    for n in range(3):
        g = Generator()
        generators.append(g)
        g.start()

    operators = []
    for n in range(6):
        o = Operator()
        operators.append(o)
        o.start()

    # waiting generators
    for g in generators:
        g.join()

    # print remains of singleton
    time.sleep(1)

    print(f"Remains[{len(settings.list_as_singleton)}] = {settings.list_as_singleton}")
    # end of program
