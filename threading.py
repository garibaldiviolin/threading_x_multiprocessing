from time import monotonic
import logging
import threading


def thread_function(name):
    """worker function"""
    start = monotonic()
    x = 0
    for _ in range(50_000_000):
        x += 1
    end = monotonic()
    print(end - start)
    return


if __name__ == "__main__":
    threads = list()
    for index in range(8):
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
