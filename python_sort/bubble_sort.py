##冒泡排序
##每次比较相邻的两个元素，若是前者比后者大，则交换两个的位置
##对数组的每一对相邻两个元素进行比较，进行n-1次比较(n为数组长度)后，最后一个元素一定是最大的数
##重复以上步骤，直至没有任何一对数字需要比较(每次都不用再比较前一次步骤中的最后一个数了)
def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
array1=[6,2,1,8,2,5,0,3,4]
print(bubble_sort(array1))
