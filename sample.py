# x = "a aa 1 aa aa aa"
# list1 = x.split(" ")
# list2 = []
# for i in range(len(list1)):
# 	if list1[i] == "1":
# 		list2.append(int(list1[i]))
# 	else:
# 		list2.append(list1[i])
# print(list2)

# formlist = []
# filehandle = open("form//easy.txt", "r")
# for i in filehandle:
# 	list3 = []
# 	l = i[:-1]
# 	list1 = l.split(" ")
# 	for j in range(len(list1)):
# 		if list1[j] == "-":
# 			list3.append(list1[j])
# 		else:
# 			x = int(list1[j])
# 			list3.append(x)
# 	formlist.append(list3)
# filehandle.close()
# print(formlist)

# for i in range(10):
# 	for j in range(10):
# 		print (formlist[i][j], end=" ")
# 	print("\n")

# a = "-" * 64
# b = "=" * 64
# for n in range(10):
# 	for m in range(10):
# 		print(formlist[n][m], end="")
# 		if m %3 == 0:
# 			print("||", end="")
# 		else:
# 			print("|",end="")
# 	if n % 3 == 0:
# 		print("\n"+b)
# 	else:
# 		print("\n"+a)

import colorama
colorama.init()
print(colorama.Fore.GREEN+"GREEN"+colorama.Fore.RESET+"normal")