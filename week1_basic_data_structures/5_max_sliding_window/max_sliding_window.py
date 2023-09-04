from collections import deque


def max_sliding_window(arr, window):
    def clean_deque(deque, i, k):
        # Remove indices that are out of the current window or
        # no longer relevant (smaller elements)
        if deque and deque[0] < i - k + 1:
            deque.popleft()

        while deque and arr[i] >= arr[deque[-1]]:
            deque.pop()

    n = len(arr)
    if n == 0:
        return []

    if window == 1:
        return arr

    max_vals = []
    max_idx = deque()

    for i in range(window):
        clean_deque(max_idx, i, window)
        max_idx.append(i)

    max_vals.append(arr[max_idx[0]])

    for i in range(window, n):
        clean_deque(max_idx, i, window)
        max_idx.append(i)
        max_vals.append(arr[max_idx[0]])

    return max_vals


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    result = max_sliding_window(input_sequence, window_size)
    print(*result)
