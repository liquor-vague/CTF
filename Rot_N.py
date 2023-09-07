def rot_n(text, n):
    result = ""
    for char in text:
        if char.isalpha():
            # 判断字符是大写还是小写
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')
            
            # 执行ROT-N变换
            rotated_char = chr((ord(char) - start + n) % 26 + start)
            result += rotated_char
        else:
            # 如果字符不是字母，则保持不变
            result += char
    return result

def main():
    choice = input("请选择操作 (1: 加密, 2: 解密): ")
    
    if choice == '1':
        text = input("请输入要加密的文本: ")
        n = int(input("请输入ROT-N的N值: "))
        encrypted_text = rot_n(text, n)
        print("加密后的文本:", encrypted_text)
    elif choice == '2':
        text = input("请输入要解密的文本: ")
        while(1):
            n = int(input("请输入ROT-N的N值: "))
            decrypted_text = rot_n(text, -n)  # 解密时将N值取负数
            print("解密后的文本:", decrypted_text)
    else:
        print("无效的选择")

if __name__ == "__main__":
    main()
