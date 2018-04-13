##快速排序
def quick_sort(array, left, right):
    if left >= right:
        return array
    key = array[left]
    i = left
    j = right
    while i < j:
        while i < j and array[j] >= key:
            j -= 1
        array[i] = array[j]
        while i < j and array[i] <= key:
            i += 1
        array[j] = array[i]
    array[j] = key
    quick_sort(array, left, i - 1)
    quick_sort(array, i + 1, right)
    return array
    
array1=[7,3,1,0,2,5,3,4]
print(quick_sort(array1,0,len(array1)-1))
