import itertools

case_list=["用户名","密码"]
value_list=["正确","不正确","特殊符合","超过最大长度"]

def gen_case(item=case_list,value=value_list):
    for i in itertools.product(item,value):
        print("输入".join(i))

def test_print():
    print("欢迎")

if __name__ == '__main__':
    test_print()