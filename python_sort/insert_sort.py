##插入排序
##我们通常将第一个元素当做已经被排序的元素，取下一个元素作为待插入已排
##序列中的元素，记作key。在已经排列的元素序列中从后往前与key进行比较，
##用j来记录当前位置，若当前位置元素比key大，则j-1，向前一位再与key进行
##比较，直到当前位置元素小于key，或者到达这个序列的顶端(当j=0时，表示走
##到这个已排序列的第一个元素)。将key插入到新的位置当中。
def insert_sort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
array1=[4,3,1,0,2,5,3]
print(insert_sort(array1))
