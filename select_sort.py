##选择排序
##将数组中第一个数字的位置用min记录，表示最小值所在位置，即将第一个数字视为当前最小值。
##将后面数字与最小值进行比较，若出现数字小于最小值，则更新min为这个数字所在位置，即将这个数字视为当前最小值。
##遍历完所有数字后，将当前最小值和第一个数字进行交换，则第一个数字是数组中最小的。
##以此类推，将数组中第二个数字的位置用min记录，后面过程与前面过程相同。
def select_sort(array):
    for i in range(len(array)):
        min = i
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]
    return array
    array1=[4,2,6,1,1,5,7,2,3]
    print(select_sort(array1))
