from datetime import datetime


class MergeManager:
    start_time = 0
    compare_count = 0
    swap_count = 0

    # sorts array elements by zoom ratio in increasing order
    @staticmethod
    def merge_sort(arr):
        MergeManager.start_time = datetime.now().microsecond
        MergeManager.compare_count = 0
        MergeManager.swap_count = 0
        # sorting
        MergeManager.sort(arr)
        # output
        print("Merge sort by zoom ratio RESULTS:")
        print("Time spent: %s mills" % (datetime.now().microsecond - MergeManager.start_time))
        print("Number of comparisons: " + str(MergeManager.compare_count))
        print("Number of item swaps: " + str(MergeManager.swap_count))
        print("Final array:")
        for j in range(len(arr)):
            print(arr[j])
        print("\n====================\n")

    @staticmethod
    def sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            MergeManager.sort(left_half)
            MergeManager.sort(right_half)

            left_iter = 0
            right_iter = 0
            iter = 0
            while left_iter < len(left_half) and right_iter < len(right_half):
                MergeManager.compare_count += 1
                MergeManager.swap_count += 1
                if left_half[left_iter].zoom_ratio < right_half[right_iter].zoom_ratio:
                    arr[iter] = left_half[left_iter]
                    left_iter += 1
                else:
                    arr[iter] = right_half[right_iter]
                    right_iter += 1
                iter += 1

            while left_iter < len(left_half):
                arr[iter] = left_half[left_iter]
                left_iter += 1
                iter += 1

            while right_iter < len(right_half):
                arr[iter] = right_half[right_iter]
                right_iter += 1
                iter += 1
