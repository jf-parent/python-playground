def qsort(array):
    if array:
        left = []
        center = []
        right = []

        pivot = array[0]
        for n in array:
            if n < pivot:
                left.append(n)
            elif n > pivot:
                right.append(n)
            else:
                center.append(n)
        return sort(left) + center + sort(right)
    else:
        return array

#print(qsort([4,3,1,2,6,7,7,9]))

def qsort_inplace(array):
    _qsort_inplace(array, 0, len(array) - 1)
    return array

def _qsort_inplace(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        _qsort_inplace(array, start, right)
        _qsort_inplace(array, left, stop)

print(qsort_inplace([4,3,1,2,6,7,7,9]))
