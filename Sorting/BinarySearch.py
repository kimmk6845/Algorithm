## binary search (이진 탐색 알고리즘) --> 순환 알고리즘
def binarySearch(a,key,left,right):
    if left <= right:
        mid = (left + right) // 2
        if key==a[mid]:
            return mid
        elif key < a[mid]:
            return binarySearch(a,key,left,mid-1)
        else:
            return binarySearch(a,key,mid+1,right)
    else:
        return -1

a=[]
while 1:
    num = int(input("리스트를 채워주세요(-1입력시 루프종료):"))
    if num == -1:
        break
    a.append(num)
key = int(input("키 값 입력:"))
index = binarySearch(a,key,0,len(a))
print("리스트 a = ",a)
print("키 값의 인덱스 = ",index)