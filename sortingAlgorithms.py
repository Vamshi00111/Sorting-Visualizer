import sys
from typing import List

class sortingAlgorithms:

    def selectionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            minIndex = i # i is our start point for unsorted array
            for j in range(i, n): # Start from i index and swap it with the minimum in the unsorted Array
                if nums[j] < nums[minIndex]: minIndex = j
            nums[i], nums[minIndex] = nums[minIndex], nums[i]
        
        return nums
    
    def insertionSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            temp = nums[i] # inserting the element
            j=i-1 # insert to the left
            while j>=0 and nums[j]> temp: # Think of everything as a pointer, can mix a while and an if, Its like 
                nums[j+1] = nums[j] # Moving the element to the right if its greater than temp and creating a slot for the temp too
                j -= 1
            nums[j+1] = temp # Fill that slot with the temp(the intended element that you wanted to insert)
        return nums
    
    def bubbleSort(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            swapped = False
            for j in range(n-i-1):
                if nums[j+1] < nums[j]: 
                    nums[j+1], nums[j] = nums[j], nums[j+1]
                    swapped = True
            if swapped == False: break #will break the loop if the array is already sorted, Making the code more efficient
            #This works because you check the every adjacent pair
        return nums
    
    def partitionForQuickSort(self, nums: List[int], IndexOfItemFromLeft: int, IndexOfItemFromRight: int) -> int:
        
        pivotLocation = IndexOfItemFromRight
        IndexOfItemFromRight -= 1

        while IndexOfItemFromLeft <= IndexOfItemFromRight: 
            # Order of these if clauses matter, first write the code of statements for which the loop is meant to be

            if nums[IndexOfItemFromRight] < nums[pivotLocation] and nums[IndexOfItemFromLeft] > nums[pivotLocation]: 
                # for the if clause order here, the if statement satisfies if left goes past right after the partition is sorted. So this order
                nums[IndexOfItemFromRight], nums[IndexOfItemFromLeft] = nums[IndexOfItemFromLeft], nums[IndexOfItemFromRight]
                IndexOfItemFromRight -= 1
                IndexOfItemFromLeft += 1
            if nums[IndexOfItemFromRight] > nums[pivotLocation]: IndexOfItemFromRight -= 1
            if nums[IndexOfItemFromLeft] < nums[pivotLocation]: IndexOfItemFromLeft += 1

        # Order of these if clauses matter
        nums[pivotLocation], nums[IndexOfItemFromLeft] = nums[IndexOfItemFromLeft], nums[pivotLocation]
        return IndexOfItemFromLeft
    

    def quickSort(self, nums: List[int], low: int, high: int) -> None: #Type hints
        if low < high:
            pivotLocation = self.partitionForQuickSort(nums, low, high)
            self.quickSort(nums, low, pivotLocation-1)
            self.quickSort(nums, pivotLocation+1, high)


    def mergeLists(self, nums1: List[int], nums2: List[int]): # Merge sorted Array problem

        i = 0
        j = 0
        k = 0
        mergedList = []
        while i< len(nums1) and j< len(nums2):
            if nums1[i] < nums2[j]:
                mergedList.append(nums1[i])
                i += 1
            elif nums2[j] < nums1[i]:
                mergedList.append(nums2[j])
                j += 1
        
        while i< len(nums1):
            mergedList.append(nums1[i])
            i += 1

        while j< len(nums2):
            mergedList.append(nums2[j])
            j += 1
       
        return mergedList
    

    def mergeSort(self, nums: List[int]) -> List[int]: 
        # First write the whole functions implementation and then write each and every detailed function
        n = len(nums)
        if n == 1 or n == 0: return nums
        
        leftSortedArray = self.mergeSort(nums[0:n//2])
        rightSortedArray = self.mergeSort(nums[n//2:n])
        
        return self.mergeLists(leftSortedArray, rightSortedArray)


if __name__ == "__main__" :
    sorter = sortingAlgorithms()
    inputArray = [64, 32, 25, 1, 4, 36]
    nums1 = sorter.mergeSort(inputArray)
    print("Sorted Array",nums1)

    nums5 = []
    sorted_nums5 = sorter.mergeSort(nums5)
    print("Sorted array is:", sorted_nums5)  # Expected output: []
    
    # Test case 6: List with negative numbers
    nums6 = [-5, 0, -3, -2, -1]
    sorted_nums6 = sorter.mergeSort(nums6)
    print("Sorted array is:", sorted_nums6)  # Expected output: [-5, -3, -2, -1, 0]
    
    # Test case 7: List with large numbers
    nums7 = [1000000, 100000, 10000, 1000, 100, 10, 1]
    sorted_nums7 = sorter.mergeSort(nums7)
    print("Sorted array is:", sorted_nums7)  # Expected output: [1, 10, 100, 1000, 10000, 100000, 1000000]
    
    # Test case 8: List with floating-point numbers
    nums8 = [3.5, 2.1, 3.9, 1.8, 2.5]
    sorted_nums8 = sorter.mergeSort(nums8)
    print("Sorted array is:", sorted_nums8)  # Expected output: [1.8, 2.1, 2.5, 3.5, 3.9]
