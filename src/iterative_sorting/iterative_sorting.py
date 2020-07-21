# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
     #starting at 2nd item, iterate through list
    for i in range(1, len(arr)):
        #num currently being sorted
        curr_num = arr[i]
        #move curr num back through arr
        j = i
        #keep moving until greater than num before OR reach start
        while j > 0 and curr_num < arr[j - 1]:
            #replace curr num with num to the left
            arr[j] = arr[j-1]
            j -= 1
        #set value of current index to curr num
        arr[j] = curr_num
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0, (len(arr) - 1)):
            if arr[i] > arr[i + 1]:
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
