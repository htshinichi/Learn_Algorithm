### 【冒泡排序】
每次比较相邻的两个元素，若是前者比后者大，则交换两个的位置。对数组的每一对相邻两个元素进行比较，进行n-1次比较(n为数组长度)后，最后一个元素一定是最大的数。重复以上步骤，直至没有任何一对数字需要比较(每次都不用再比较前一次步骤中的最后一个数了)
例如对序列6、2、1、8、2、5、0、3、4进行排列:
![这里写图片描述](https://img-blog.csdn.net/20180412104655970?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM1OTc5MzE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 【直接选择排序】
将数组中第一个数字的位置用min记录，表示最小值所在位置，即将第一个数字视为当前最小值。将后面数字与最小值进行比较，若出现数字小于最小值，则更新min为这个数字所在位置，即将这个数字视为当前最小值。遍历完所有数字后，将当前最小值和第一个数字进行交换，则第一个数字是数组中最小的。以此类推，将数组中第二个数字的位置用min记录，后面过程与前面过程相同。
例如对序列6、2、1、8、2、5、0、3、4进行排列:
![这里写图片描述](https://img-blog.csdn.net/20180412111804327?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM1OTc5MzE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 【直接插入排序】
我们通常将第一个元素当做已经被排序的元素，取下一个元素作为待插入已排序列中的元素，记作key。在已经排列的元素序列中从后往前与key进行比较，用j来记录当前位置，若当前位置元素比key大，则j-1，向前一位再与key进行比较，直到当前位置元素小于key，或者到达这个序列的顶端(当j=0时，表示走到这个已排序列的第一个元素)。将key插入到新的位置当中。
例如对序列6、2、1、8、2、5、0、3、4进行排列:
![这里写图片描述](https://img-blog.csdn.net/20180412115904364?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM1OTc5MzE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


### 【快速排序】
每一趟排序都会选择一个基准数，标记为key，一般为了方便选择第一个数作为基准数，当然也可以随机选取。然后我们设定两个哨兵i和j，分别从待排序序列的左边和右边同时向对面前进。左边哨兵i找到一个比key大(或相等)的数就停下来，右边哨兵j找到一个比key小(或相等)的数就停下来，交换这两个数。然后哨兵i继续向右走，哨兵j继续向左走，直到i$\ge$j，我们将key与i所在位置的元素交换。这样我们会发现key的左边都是小于等于它的数字，而右边都是大于等于它的数字。然后递归地对左右两边的子序列按照上面的步骤进行排序，直至拆分不出新的子序列为止。
例如对序列6、2、1、8、2、5、0、3、4进行排列:
![这里写图片描述](https://img-blog.csdn.net/20180412125018999?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM1OTc5MzE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)

### 【归并排序】
归并排序采用了典型的分治策略，将待排序列拆分成一个一个的子序列，再将这些子序列合并成有序序列。
例如对序列6、2、1、8、2、5、0、3、4进行排列:
![这里写图片描述](https://img-blog.csdn.net/20180412135118413?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM1OTc5MzE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)


## 复杂度

![这里写图片描述](https://img-blog.csdn.net/20180412152614105?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3UwMTM1OTc5MzE=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
