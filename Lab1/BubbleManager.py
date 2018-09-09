from datetime import datetime


class BubbleManager:
    # sorts array elements by memory size in decreasing order
    @staticmethod
    def bubble_sort(arr):
        start_time = datetime.now().microsecond
        compare_count = 0
        swap_count = 0
        # sorting
        for k in range(len(arr)):
            for i in range(k):
                compare_count += 1
                if arr[i].memory < arr[i + 1].memory:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swap_count += 1
        # output
        print("Bubble sort by memory RESULTS:")
        print("Time spent: %s mills" % (datetime.now().microsecond - start_time))
        print("Number of comparisons: " + str(compare_count))
        print("Number of item swaps: " + str(swap_count))
        print("Final array:")
        for j in range(len(arr)):
            print(arr[j])
        print("\n====================\n")
