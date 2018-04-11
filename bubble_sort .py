def bubble_sort(lists):
    cout=len(lists)
    for i in range(count):
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists
        

lists=[2,3,1,0,2,5,3]
print(bubble_sort(lists))
