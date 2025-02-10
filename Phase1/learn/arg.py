import sys
print(f"程序名称：{sys.argv[0]}")
arg_count = len(sys.argv) - 1
print(f"传递参数的数量是：{arg_count}")
print(f"sys.argv 的类型是：{type(sys.argv)}")
if arg_count > 0:
    for i, arg in enumerate(sys.argv[1:], start = 1):
        print(f"参数 {i} 是：{arg}")
else:
    print("此程序没有参数。")