def balancedSum(arr):
    
    index = 0
    left_sum = 0
    right_sum = sum(arr[index+1:])

    while True:
      if left_sum == right_sum:
        return index

      else:
        left_sum += arr[index]
        right_sum -= arr[index+1]
        index += 1
      
      if index == len(arr):
        return index


balancedSum([1,2,3,3])


#기준값 좌,우 합 같은 문제


#슬라이딩 윈도우  
#시작,끝 포인터 같은 곳에서 출발
#이동하면서 한개씩 더하고 뺴주기
