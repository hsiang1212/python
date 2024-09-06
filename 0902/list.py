score=[100,60,70,90,40,66]

#取列表中的第0位
print(score[0])

#列表新增值於最後一位
score.append(66)
print(score)

#列表新增值於指定位置
score.insert(1,77)
print(score)

#列表刪除某個值
score.remove(100)
print(score)

#列表裡的值要更新
score[1]=55
print(score)