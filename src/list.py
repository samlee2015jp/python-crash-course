# 空列表
my_list = []

# 含有元素的列表
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]

# 列表中可以混合类型
mixed = [1, "apple", True, 3.14]

# 访问元素（索引从0开始）
print(fruits[0])  # 输出 "apple"
print(fruits[-1]) # 输出 "cherry"，负数表示从尾部开始

# 修改元素
fruits[1] = "blueberry"
print(fruits)  # ["apple", "blueberry", "cherry"]

# 添加元素
fruits.append("orange")  # 添加到末尾
fruits.insert(1, "kiwi")  # 在索引1处插入
print(fruits)

# 删除元素
fruits.pop()  # 删除末尾元素
fruits.pop(1) # 删除索引1元素
fruits.remove("apple")  # 删除指定值
print(fruits)

# 列表长度
print(len(fruits))  # 输出元素数量

# 遍历列表
for fruit in fruits:
    print(fruit)

# 判断元素是否在列表中
if "apple" in fruits:
    print("Yes")

# 列表排序
numbers.sort()  # 升序排序
numbers.sort(reverse=True)  # 降序排序

# 复制列表
copy_list = fruits.copy()

# 清空列表
fruits.clear()
print(fruits)
print(copy_list)
