from BubbleManager import BubbleManager
from MergeManager import MergeManager
from Camera import Camera


class Main:
    ARRAY_SIZE = 100
    INDEX_PRODUCER = 0
    INDEX_MEMORY = 1
    INDEX_ZOOM_RATIO = 2
    cameras = [Camera()] * ARRAY_SIZE

    @staticmethod
    def init():
        with open("cameras.txt") as file:
            i = 0
            for line in file:
                array = line.split(",")
                Main.cameras[i] = Camera(array[Main.INDEX_PRODUCER], int(array[Main.INDEX_MEMORY]),
                                         float(array[Main.INDEX_ZOOM_RATIO]))
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
