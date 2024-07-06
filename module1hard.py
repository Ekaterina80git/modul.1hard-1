# дано- grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
#students ={"Jonni",'Bilbo",'Steve","Khendrik","Aaron"}
#список садержит оценки учеников в алфавитном порядке множество неупорядочено
# создать словарь где имя - ключ, значение - средний бал ученика
#
grades= [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]]
students = {"Jonni","Bilbo","Steve","Khendrik","Aaron"}
magazin = {"Aaron":[5,3,3,5,4],"Bilbo":[2,2,2,3],"Jonni":[4,5,5,2],"Khendrik":[4,4,3],"Stive":[5,5,5,4,5]}


a = sum(grades[0])
a_1 = (int(a)//5)
magazin["Aaron"] = a_1
print(magazin)
b = sum(grades[1])
b_1 = (float(b)/4)
magazin["Bilbo"] = b_1
c = sum(grades[2])
c_1 = (int(c)//4)
magazin["Jonni"]= c_1
d = sum(grades[3])
d_1 = (float(d)/3)
magazin["Khendrik"] = d_1
f = sum(grades[4])
f_1 = (float(f)/5)
magazin["Stive"] = f_1
print(magazin)






