from threading import *
from time import sleep


class thread_function1(Thread):
    def run(self):
        for i in range(5):
            print('I am in the multi thread function 1')
            sleep(0.2)


class thread_function2(Thread):
    def run(self):
        for i in range(5):
            print('I am in the multi thread function 2')
            sleep(0.2)


thread1 = thread_function1()
thread2 = thread_function2()

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('You can see above that the 2 threads are executed parallel and NOT sequentially based on print statements')
print('Finished both the threads')
