# insertion sort: find the minimum in unsorted and swap down until correct

def ins_sort(arr):
    for x in range(0, len(arr) - 1):
        y = x + 1
        while y > 0:
            if arr[y] < arr[y - 1]:
                temp = arr[y]
                arr[y] = arr[y - 1]
                arr[y - 1] = temp
                y -= 1
            else:
                break
    return arr


# selection sort: find the minimum in unsorted and swap down instantly
def sel_sort(arr):
    x = 0
    while x < len(arr):
        min_pos = x
        for y in range(x, len(arr)):
            if arr[y] < arr[min_pos]:
                min_pos = y
        temp = arr[min_pos]
        arr[min_pos] = arr[x]
        arr[x] = temp
        x += 1
    return arr


test_arr = [1, 12, 9, 7, 3, 6, 11]


print(ins_sort(test_arr))
print(sel_sort(test_arr))

