def correct_ip(ip):
    if len(ip) != 4:
        print("Адрес — это четыре числа, разделённые точками.")
        return

    for element_ip in ip:
        if not element_ip.isdigit():
            print(f"{element_ip} — это не целое число.")
            return
        if int(element_ip) > 255:
            print(f"{element_ip} превышает 255.")
            return
        if int(element_ip) < 0:
            print(f"{element_ip} меньше 0.")
            return
    print("IP-адрес корректен.")


ip_user = input("Введите IP: ").split('.')
correct_ip(ip_user)
