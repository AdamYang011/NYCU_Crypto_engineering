def cal_IC(text):
    text_num = len(text)
    number = {}
    tmp = 0

    for i in sorted(text):
        number[i] = text.count(i)

    for i in number.keys():
        tmp += number[i] * (number[i]-1)
    IC = tmp / (text_num * (text_num-1))

    print("%.5f" % IC)

while(1):
    case_num = input("Please input your case number: ")  #Q3_1,Q3_2,Q3_3,Q3_4,Q4
    str = "test" + case_num + ".txt"

    f = open(str, 'r')
    text = f.read()
    f.close()
    text = text.replace(" ","")
    text = text.replace("\n","")
    text = text.replace(",","")
    cal_IC(text)