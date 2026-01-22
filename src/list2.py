# 空リスト
my_list = []

# 要素を含むリスト
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
print(numbers[0])    # 1
print(fruits[-1])    # "cherry"
print(numbers[1:4])  # [2, 3, 4]
for fruit in fruits:
    print(fruit)
print(len(fruits))   # 3
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)  # [2, 4]
def get_numbers():
    return [10, 20, 30]

nums = get_numbers()
print(nums)  # [10, 20, 30]
