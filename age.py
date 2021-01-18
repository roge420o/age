driving = input("請問你有沒有開過車?")
if driving != "有" and driving != "沒有":
    print("只能輸入 有/沒有")
    raise SystemExit
    
age = input("請你的年齡?")
age = int(age)
if driving == "有":
    if age >= 18:
        print("你通過測驗了")
    else:
        print("奇怪 你怎麼有開過車")
elif driving == "沒有":
    if age >= 18:
        print("你可以考駕照了阿，怎麼還不去考")
    else:
        print("再過幾年就可以考囉")
else:
    print("只能輸入有/沒有")