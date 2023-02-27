def converter_to_f(celsius_value):
    return celsius_value *0.9 / 5 +32

# 작점 실행 할때만 __main__ 여기에 실행된다.
if __name__ == "__main__":
    print('test==>',converter_to_f(20))
else:
    print("Thank for using my module!")