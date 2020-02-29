import threading


class PrintThread(threading.Thread):
    def run(self):
        for i in range(1, 11):
            print(i)


print("Current Thread : ", threading.current_thread())
t1 = PrintThread()
t1.start()
print("Count of threads :", threading.activeCount())
print("The End!")