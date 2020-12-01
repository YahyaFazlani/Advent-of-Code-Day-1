import mylist


def findTotal(input: list, total: int):
  for i in range(len(input)):
    number_to_find = total - input[i]
    if number_to_find in input:
      print(f"{input[i]} + {number_to_find} = 2020")
      print(f"Product: {input[i] * number_to_find}")


findTotal(mylist.numbers_list, 2020)
