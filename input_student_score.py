#輸入班級數
num_class = input('請輸入班級數')

#儲存所有成績的資料組
all_score_list = []

for i in range (0,num_class)
    print('第',i+1,'班') #印出第一班、第二班....
    
    #輸入班級人數
    num_student = input('請輸入班級人數')
    
    #儲存單一班級成績的資料組
    score_list = []
    #依序輸入每個學生得成績
    for j in range (0,num_student)
        score = int(input('輸入學生的成績'))
        score_list.extend([score])
        
    #存入班級的成績
    all_score_list.extend(score_list)
#印出所有班級和學生成績
for i, score_list in enumerate #enumerate用法==>enumerate(sequence, [start=0])
    print('第'i+1,'班學生的成績',score_list)
    