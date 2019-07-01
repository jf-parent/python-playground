def sort(array):
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

print(sort([4,3,1,2,6,7,7,9]))
