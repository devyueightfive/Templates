# singletons
import threading
list_as_singleton = []
shared_counter = 0
generator_lock = threading.Lock()
operator_lock = threading.Lock()
