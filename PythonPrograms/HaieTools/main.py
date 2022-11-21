
if __name__ == '__main__':
    while True:
        command = input("请输入指令：")
        if command == "0":
            res = input("是否确认退出？Y/N")
            if res == "Y" or res == "y":
                break
            else:
                continue
        print("程序运行了！")
