def main():
    algorithms = [
        "Linear Search",
        "Binary Search",
        "Bubble Sort",
        "Selection Sort",
        "Insertion Sort",
        "Merge Sort",
        "Quick Sort",
        "Heap Sort",
        "Radix Sort",
        "Counting Sort",
        "Breadth-First Search (BFS)",
        "Depth-First Search (DFS)",
        "Dijkstra's Algorithm",
        "A* Search Algorithm",
        "Kruskal's Algorithm",
        "Prim's Algorithm",
        "Bellman-Ford Algorithm",
        "Floyd-Warshall Algorithm",
        "Topological Sort",
        "Knapsack Problem (Dynamic Programming)",
        "Longest Common Subsequence (Dynamic Programming)",
        "Minimum Spanning Tree (MST)",
        "Graph Coloring",
        "K-means Clustering",
        "Convex Hull (Graham's Scan)"
    ]

    print("Choose an algorithm to execute:")
    for i, algorithm in enumerate(algorithms, 1):
        print(f"{i}. {algorithm}")

    choice = int(input("Enter the number of the algorithm: "))

    if 1 <= choice <= len(algorithms):
        algorithm_index = choice - 1
        algorithm_name = algorithms[algorithm_index]
        print(f"\nExecuting {algorithm_name}...\n")

        if algorithm_name == "Linear Search":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            target = int(input("Enter the target value: "))
            result = linear_search(arr, target)
            print(f"Result: {result}")

        elif algorithm_name == "Binary Search":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            target = int(input("Enter the target value: "))
            result = binary_search(arr, target)
            print(f"Result: {result}")

        elif algorithm_name == "Bubble Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            bubble_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Selection Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            selection_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Insertion Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            insertion_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Merge Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            merge_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Quick Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            quick_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Heap Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            heap_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Radix Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            radix_sort(arr)
            print(f"Sorted Array: {arr}")

        elif algorithm_name == "Counting Sort":
            arr = list(map(int, input("Enter the array (space-separated): ").split()))
            counting_sort(arr)
            print(f"Sorted Array: {arr}")

        else:
            print("Algorithm not implemented in the main program.")
    else:
        print("Invalid choice. Please enter a number between 1 and", len(algorithms))


###############################################
# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


###############################################
# Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


##############################################
# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


###############################################
# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


###############################################
# Insertion Sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


###############################################
# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


###############################################
# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


###############################################
# Heap Sort
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


###############################################
# Radix Sort
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10


###############################################
# Counting Sort

def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    i = 0
    for j in range(max_val + 1):
        while count[j] > 0:
            arr[i] = j
            count[j] -= 1
            i += 1


##############################################
if __name__ == "__main__":
    main()