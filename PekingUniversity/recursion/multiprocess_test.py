import os
from multiprocessing import Process, Value, Array


procs = 3
count = 0


def show_data(label, val, arr):
    msg = "%-12s: pid: %4s, global:%s, value: %s, array:%s"
    print("Process Array", list(arr))
    print(msg % (label, os.getpid(), count, val.value, list(arr)))


def updater(val, arr):
    global count
    count += 1
    val.value += 1
    print("Val", val.value)
    for i in range(3):
        arr[i] += 1
    print("Process Array", list(arr))


if __name__ == "__main__":
    scalar = Value("i", 0)
    vector = Array("d", procs)
    ("parent start", scalar, vector)
    show_data("parent", scalar, vector)
    p = Process(target=show_data, args=("child", scalar, vector))
    p.start()
    p.join()
    print('\nloop1 (updates in parent, serial children)')
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=show_data, args=(("process %s" % i), scalar, vector))
        p.start()
        p.join()
    print("Value:", scalar.value)
    print("Array:", list(vector))
    print('\nloop2 (updates in parent, parallel children)')
    ps = []
    for i in range(procs):
        count += 1
        scalar.value += 1
        vector[i] += 1
        p = Process(target=show_data, args=(("process %s" % i), scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    print("Value:", scalar.value)
    print("Array:", list(vector))
    print('\nloop3 (updates in serial children)')
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        p.join()
    show_data("parent temp", scalar, vector)

    print('\nloop4 (updates in parallel children)')
    ps = []
    for i in range(procs):
        p = Process(target=updater, args=(scalar, vector))
        p.start()
        ps.append(p)
    for p in ps:
        p.join()
    show_data("parent end", scalar, vector)
