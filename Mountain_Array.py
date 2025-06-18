class Mountain_Array(object):
    def __init__ (self,arr):
        self.arr = arr
    def peakIndexinMountainArr(self):
        left,right = 0, len(self.arr)-1 #start indexing at 0
        while left < right:  #create logic for right being greater than left
            mid = (left+right)// 2
            if self.arr[mid]<self.arr[mid+1]:  #start ascension, moves right
                left = mid + 1
            else:                   #start decension moves left
                right = mid
        return left
mountain = Mountain_Array([0,5,10,2])  #checks peak index and returns it
print(mountain.peakIndexinMountainArr())


