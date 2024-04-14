# 定义一个函数，用于算法生成指定数量的勾股三元组
def generate_pythagorean_triplet_euclid(limit):
    # 初始化一个空列表，用于存储生成的勾股三元组
    triplets = []
    # 初始化m和n的值，它们是用于生成勾股三元组的两个变量
    m, n = 2, 1

    # 当生成的三元组数量少于指定的limit时，继续循环
    while len(triplets) < limit:
        # 使用欧几里得公式生成三个数
        a = m ** 2 - n ** 2
        b = 2 * m * n
        c = m ** 2 + n ** 2

        # 检查生成的三个数是否满足勾股定理
        if a ** 2 + b ** 2 == c ** 2:
            # 如果满足，则将该三元组添加到列表中
            triplets.append((a, b, c))

            # 更新m的值，并检查m和n的最大公约数
        m += 1
        # 如果m和n不互质（即最大公约数不为1），则重置n的值为1
        if gcd(m, n) != 1:
            n = 1
        else:
            # 如果m和n互质，则增加n的值
            n += 1

            # 为了避免生成过大的数，设置一个条件来提前终止循环
        if m * n > limit * 10:
            break

            # 返回生成的三元组列表
    return triplets


# 定义一个函数，用于计算两个数的最大公约数
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# 设置生成的三元组的数量
limit = 1000
# 调用函数生成勾股三元组
pythagorean_triplets = generate_pythagorean_triplet_euclid(limit)

# 验证生成的三元组是否满足勾股定理
invalid_triplets = []
for triplet in pythagorean_triplets:
    a, b, c = triplet
    if a ** 2 + b ** 2 != c ** 2:
        # 如果不满足，则添加到无效三元组列表中
        invalid_triplets.append(triplet)

    # 验证生成的三元组是否符合勾股定理
if invalid_triplets:
    print("Invalid triplets found:", invalid_triplets)
else:
    print("All triplets satisfy the Pythagorean theorem.")

# 将有效的勾股三元组保存到TXT文件中
with open('pythagorean_triplets.txt', mode='w') as file:
    file.write("a,b,c\n")  # 写入表头，表示三个数分别是a, b, c
    for triplet in pythagorean_triplets:
        # 写入每个三元组，格式为CSV，每个三元组占一行
        file.write(f"{triplet[0]},{triplet[1]},{triplet[2]}\n")

    # 打印保存结果的信息
print(f"Results saved to 'pythagorean_triplets.txt'")