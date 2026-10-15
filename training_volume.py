# #计算健身容量
# print ("引体向上 对握高位下拉 划船 俯身划船 反向坐姿飞鸟")
# print ("引体自身体重  对握60kg 划船70kg 附身划船70kg 反向坐姿飞鸟50kg")
# print ("引体向上 4组 10次 对握高位下拉 4组 10次 划船 4组 10次 俯身划船 4组 10次 反向坐姿飞鸟 4组 10次")
# heavy = float(input("请输入你的体重(kg):"))
# print (f"本次训练的健身容量为：{heavy * 4 * 5 + 60 * 4 * 10 + 70 * 4 * 10 + 70 * 4 * 10 + 50 * 4 * 10}kg")

boby_weight = float(input("请输入你的体重(kg):"))
pull_up = float(input("请输入你引体向上的重量(kg):"))
row = float(input("请输入你划船的重量(kg):"))
bent_over_row = float(input("请输入你俯身划船的重量(kg):"))
seated_fly = float(input("请输入你反向坐姿飞鸟的重量(kg):"))
total_volume =(
    boby_weight * 4 * 10 + pull_up * 4 * 10 + row * 4 * 10 + bent_over_row * 4 * 10 + seated_fly * 4 * 10
)
print(f"本次训练的健身容量为：{total_volume}kg")