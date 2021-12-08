## cocktailShakerSort(칵테일 쉐이커 정렬)
# 0번 인덱스는 더미
def cocktailShakerSort(a,n):
    check = True    # 교환이 발생했는지 확인하는 변수
    start = 1       # 시작인덱스
    end = n         # 끝인덱스
    # start와 end는 한번 반복이 끝나면 양 끝이 정렬된 것이므로
    # start는 1증가하고 end는 1감소해야 함

    while check==True:
        check=False
        for i in range(start, end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1],a[i]
                check = True
        #print(a)

        if not check:   # 교환이 발생하지 않았으니 정렬된 상태임
            break

        check = False

        for i in range(end-1,start-1,-1):   # 가장 큰 원소 옮겼으니 n-1부터 1번 인덱스 까지
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                check = True
        start += 1  # 교환이 끝나면 시작 인덱스를 증가시키고
        end -= 1    # 끝인덱스를 감소함
        #print(a)

def checkSort(a,n):
    isSorted = True
    for i in range(1,n):
        if a[i] > a[i+1]:
            isSorted = False
        if not isSorted:
            break
    if isSorted:
        print("정렬 완료")
    else:
        print("정렬 오류 발생")

# a=[None,6,5,4,3,2,1]
# n = 6
# cocktailShakerSort(a,6)

import random, time
print("#랜덤")
n=15000
a=[None]
for i in range(n):
    a.append(random.randint(1,n))
start = time.time()
cocktailShakerSort(a,n)
finish=time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,n)

print("#역순")
a=[None]
for i in range(n,0,-1):
    a.append(i)
start = time.time()
cocktailShakerSort(a,n)
finish=time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,n)

print("#정렬")
start = time.time()
cocktailShakerSort(a,n)
finish = time.time() - start
print('정렬하는데 걸린 시간 : %0.3f' %finish)
checkSort(a,n)