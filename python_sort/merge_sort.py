##归并排序        
def MergeSort(array):
    if len(array) <= 1:
        return array
    num = int( len(array) / 2 )
    left = MergeSort(array[:num])
    right = MergeSort(array[num:])
    return Merge(left,right)
def Merge(left,right):
    l, r = 0, 0
    result=[]
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
    array1=[7,3,1,0,2,5,3,4]
    print(MergeSort(array1))
