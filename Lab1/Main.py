from BubbleManager import BubbleManager
from MergeManager import MergeManager
from Camera import Camera


class Main:
    ARRAY_SIZE = 100
    cameras = [Camera()] * ARRAY_SIZE

    @staticmethod
    def init():
        with open("cameras.txt") as file:
            i = 0
            for line in file:
                array = line.split(",")
                Main.cameras[i] = Camera(array[0], int(array[1]), float(array[2]))
                i += 1

    @staticmethod
    def print_array(arr_name, arr):
        print("\n" + arr_name + ":")
        for arr_i in range(len(arr)):
            print(arr[arr_i], end="\n")
        print("\n====================\n")


Main.init()
Main.print_array("Initial array", Main.cameras)

BubbleManager.bubble_sort(Main.cameras)
MergeManager.merge_sort(Main.cameras)
