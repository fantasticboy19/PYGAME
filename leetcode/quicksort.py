import sys
sys.setrecursionlimit(10000)
def partition(a, left, right):
    if not isinstance(a, list):
        raise TypeError('this is needed to be a list')
    base = a[right]
    print(f'from {left} to {right}, we choose the base {base}')
    i = left - 1
    for j in range(left, right):
        if a[j] <= base:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[right] = a[right], a[i + 1]

    return i + 1


def quick_sort(a, left, right):
    if left < right:
        mid = partition(a, left, right)
        quick_sort(a, left, mid - 1)
        quick_sort(a, mid + 1, right)


def merge_sort(a, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(a, l, m)
        merge_sort(a, m+1, r)
        merge(a, l, m, r)


def merge(a, l, m, r):
    a_left = sorted(a[l:m])
    a_right = sorted(a[m:r])
    left_length = len(a_left)
    right_length = len(a_right)
    i = 0
    j = 0
    k = l
    while i < left_length and j < right_length:
        if a_left[i] < a_right[j]:
            a[k] = a_left[i]
            i += 1
        else:
            a[k] = a_right[j]
            j += 1
        k += 1
    while i < left_length:
        a[k] = a_left[i]
        i += 1
        k += 1
    while j < right_length:
        a[k] = a_right[j]
        i += 1
        k += 1


if __name__ == '__main__':
    demo_data = [12, 3, 20, 1, 5, 17, 14, 2, 6, 16]
    # quick_sort(demo_data, 0, len(demo_data) - 1)
    merge_sort(demo_data, 0, len(demo_data)-1)
    print(demo_data)

