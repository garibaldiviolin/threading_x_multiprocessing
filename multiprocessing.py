from time import monotonic
import multiprocessing


def worker():
    """worker function"""
    start = monotonic()
    x = 0
    for _ in range(50_000_000):
        x += 1
    end = monotonic()
    print(end - start)


if __name__ == '__main__':
    jobs = []
    for i in range(8):
        p = multiprocessing.Process(target=worker)
        jobs.append(p)
        p.start()

    for process in jobs:
        process.join()
