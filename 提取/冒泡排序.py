
'''
    排序是计算机程序设计的一种重要操作，他的功能是将一个数据元素的任意序列，重新排列成一个关键字有序的序列
    简单来说就是将一组无序的数据通过某种算法然后使他们按照某种规则有序的排列

'''
'''
    冒泡排序：是一种计算机科学领域的较简单的排序算法。它重复地走访过要排序的元素列，依次比较两个相邻的元素
    一层一层的将较大的元素往后移动。
    算法思想：从第一个和第二个开始比较，如果第一个比第二个大，则交换位置，然后比较第二个和第三个，逐渐往后
            经过第一轮后最大的元素已经排在最后，所以重复上述操作的话第二大就会排在第二个位置
            以此类推，重复操作n-1次即可完成排序

'''

def bublle_sort(arr):
    for i in range(len(arr)-1):# 控制外层循环次数
        for j in range(len(arr)-1-i):# 比较具体的两个元素
            if arr[j]>arr[j+1]: # 如果前一个元素大于后一个元素
                arr[j],arr[j+1] = arr[j+1],arr[j] # 则互换位置


    return arr


if __name__ == '__main__':
    result = bublle_sort([1,5,7,9,4])
    print(result)