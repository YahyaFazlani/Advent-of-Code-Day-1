import mylist
import math

def findTotal(input: list, total: int):
  size = len(input)
  min_diff = abs(input[0] + input[1] + input[2]-total)
  best_difference = input[0] + input[1] + input[2]
  for i in range(size):
    for j in range(i + 1, size):
      for k in range(i + 2, size):
        new_diff = abs(input[i] + input[j] + input[k] - total)
        if new_diff < min_diff:
          min_diff = new_diff
          best_till_now = input[i] + input[j] + input[k]
          if min_diff == 0:
            print(f"{input[i]} + {input[j]} + {input[k]} = 2020")



findTotal(mylist.numbers_list, 2020)
