"""Selection sort algorithm implementation."""


def selection_sort_in_place(arr: list[int]) -> None:
    """Sorts the array in place using selection sort algorithm."""
    n = len(arr)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    lst = [64, 34, 25, 12, 22, 11, 90]
    selection_sort_in_place(lst)
    print("Sorted array is:", lst)
