def my_sum(*args):
    # args 是一个元组，例如 (1, 2, 3)
    return sum(args)

print(my_sum(1, 2, 3))  # 输出: 6

def print_info(**kwargs):
    # kwargs 是一个字典，例如 {'name': 'Sam', 'age': 30}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Sam", city="Matsudo") 
# 输出:
# name: Sam
# city: Matsudo