def solve_square(a,b,c):
    number_question = input("請輸入二元方程式的係數(每一個係數之間必須空一格):")
    a, b, c = number_question.split()#將input的係數分配給a, b, c
    d = -1
    #將得到得參數由str轉成int
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    number_answer_plus = (b*d+(b**2-4*a*c)**0.5)/(a*2) #利用二元一次方程式的公式解
    number_answer_minus = (b*d-(b**2-4*a*c)**0.5)/(a*2) #減號
    return(number_answer_plus,number_answer_minus)

