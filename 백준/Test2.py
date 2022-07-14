def countPairs(numbers, k):
  dictionary = {}

  numbers = sorted(numbers)
  start_index = 0
  end_index = 0

  count = 0
  while True:

    if numbers[start_index] + k == numbers[end_index]:
      str_value = " ".join([str(numbers[start_index]),str(numbers[end_index])])
      if str_value not in dictionary:
        count += 1
        dictionary[str_value] = 1

      end_index += 1
    
    elif numbers[start_index] + k > numbers[end_index]:
      end_index += 1

    elif numbers[start_index] + k < numbers[end_index]:
      start_index += 1


    if start_index == len(numbers) or end_index == len(numbers):
      break
  
  return count



print(countPairs([1,1,2,2,3,3],1))



#투포인터 문제 
#2개의 쌍, 중복되지 않는 쌍, a+k=b 몇개인지 찾기

