from typing import List

def sortArr(lists:List[int]) -> List[int]:
    for i,item in enumerate(lists):
        for j in range(len(lists)):
            if(i<len(lists)-1 and j<len(lists)-1):
                if(list[j]>lists[j+1]):
                    temp = lists[j]
                    lists[j]=lists[j+1]
                    lists[j+1]=temp

    return lists


list = [4,8,5,3,1,22,2]
print(sortArr(list))