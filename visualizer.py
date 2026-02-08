import matplotlib.pyplot as plt
import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                yield arr

def visualize_sort():
    arr = [random.randint(1, 100) for _ in range(20)]
    generator = bubble_sort(arr)

    plt.ion()
    fig, ax = plt.subplots()
    bars = ax.bar(range(len(arr)), arr)

    for arr in generator:
        for bar, val in zip(bars, arr):
            bar.set_height(val)
        plt.pause(0.1)

    plt.ioff()
    plt.show()

if __name__ == "__main__":
    visualize_sort()
