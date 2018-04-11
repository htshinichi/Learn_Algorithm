def bubble_sort(lists):
    count=len(lists)
    for i in range(count):
        for j in range(i+1,count):
            if lists[i]>lists[j]:
                lists[i],lists[j]=lists[j],lists[i]
    return lists
        

lists=[5,3,1,0,2,4,7]
print(bubble_sort(lists))
