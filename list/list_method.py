#List is a container of various data types 
#it can store string, boolian expression , integer, float etc

zunaider_patri = ["Fatima","tuba","sadiya"]

zunaider_patrir_boyosh = [13,14,15]


zunaider_patri.append("khadiza")#kono list er "sheshe" kono datatype add korar jonne .append() use kora hoy 

#.insert(indexnum,datatype) first a boshe index number ar second a boshe kon datatype boshate chai ta
zunaider_khabar = ["Vaat","Mas","Mangsho"]

#.insert(indexnumber,datatype) insert method et first a jei shonkha thake sheda hocche oi index number tarpore koma diye ja boshe oda hocche datatype
zunaider_khabar.insert(1,["bou",3])
print(zunaider_khabar)




zunaider_patrir_boyosh.sort()
print(zunaider_patrir_boyosh)

zunaider_patri.pop(1)#kono list er moddher jekono index er datatype baad deoa jai ei .pop() method dara

print(zunaider_patri)

zunaider_patrir_boyosh.remove(14)#kono list er moddher jekhono datatype baad deoar jonne use hoy
print(zunaider_patrir_boyosh)




