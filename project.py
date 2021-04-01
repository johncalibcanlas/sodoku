import colorama
colorama.init()
def sheet (list1):
	a = "-" * 64
	b = "=" * 64
	for n in range(10):
		for m in range(10):
			print("  ", end="")
			if type(list1[n][m]) == str:
				print(colorama.Fore.GREEN+list1[n][m]+colorama.Fore.RESET,end="")
			else:
				print(list1[n][m], end="")
			print("  ",end="")
			if m %3 == 0:
				print("||", end="")
			else:
				print("|",end="")
		if n % 3 == 0:
			print("\n"+b)
		else:
			print("\n"+a)

def setsheet (file1):
	filehandle = open(file1, "r")
	for i in filehandle:
		list3 = []
		l = i[:-2]
		list1 = l.split(" ")
		for j in range(len(list1)):
			if list1[j] == "-":
				list3.append(list1[j])
			else:
				x = int(list1[j])
				list3.append(x)
		formlist.append(list3)
	filehandle.close()
def setsheet2 (file1):
	filehandle = open(file1, "r")
	for i in filehandle:
		list3 = []
		l = i[:-2]
		list1 = l.split(" ")
		for j in range(len(list1)):
			if list1[j] == "-":
				list3.append(list1[j])
			else:
				x = int(list1[j])
				list3.append(x)
		originallist.append(list3)
	filehandle.close()

def loadsetsheet(file1,file2):
	form1 = []
	form2 = []
	filehandle = open(file1, "r")
	for i in filehandle:
		list3 = []
		l = i[:-2]
		list1 = l.split(" ")
		for j in range(len(list1)):
			if list1[j] == "-":
				list3.append(list1[j])
			else:
				x = int(list1[j])
				list3.append(x)
		form1.append(list3)
	#print(form1)
	filehandle.close()
	filehandle = open(file2, "r")
	for i in filehandle:
		list3 = []
		l = i[:-2]
		list1 = l.split(" ")
		for j in range(len(list1)):
			if list1[j] == "-":
				list3.append(list1[j])
			else:
				x = int(list1[j])
				list3.append(x)
		form2.append(list3)
	#print(form2)
	filehandle.close()
	for i in range(len(list1)):
		list4 = []
		for j in range(len(list1)):
			if form1[i][j] != form2[i][j]:
				list4.append(str(form1[i][j]))
			elif form1[i][j] == "-":
				list4.append(str(form1[i][j]))
			else:
				list4.append(int(form1[i][j]))
		formlist.append(list4)

def convertint(formlist):
	checklist = []
	for i in range(10):
		checklist1 = []
		for j in range(10):
			if type(formlist[i][j]) == str:
				if formlist[i][j] == "-":
					checklist1.append(0)
				else:
					checklist1.append(int(formlist[i][j]))
			else:
				checklist1.append(formlist[i][j])
		checklist.append(checklist1)
	return checklist

def checking(checklist):
	for i in range(1,10):
		lista = []
		listb = []
		for j in range(1,10):
			lista.append(checklist[i][j])
			listb.append(checklist[j][i])
		if sum(lista) != 45:
			return False
		if sum(listb) != 45:
			return False
	if box(1,4,1,4) == 1:
		return False
	if box(1,4,4,7) == 1:
		return False
	if box(1,4,7,10) == 1:
		return False
	if box(4,7,1,4) == 1:
		return False
	if box(4,7,4,7) == 1:
		return False
	if box(4,7,7,10) == 1:
		return False
	if box(7,10,1,4) == 1:
		return False
	if box(7,10,4,7) == 1:
		return False
	if box(7,10,7,10) == 1:
		return False
	return True

def box(a,b,c,d):
	list1 = []
	for i in range(a,b):
		for j in range(c,d):
			list1.append(checklist[i][j])
	if sum(list1) != 45:
		return 1

def save(list1,list2):
	filehandle = open("form//save.txt","w")
	for i in range(10):
		for j in range(10):
			filehandle.write(str(list1[i][j]) + " ")
		filehandle.write("\n")
	filehandle.close()
	filehandle = open("form//savecompare.txt","w")
	for i in range(10):
		for j in range(10):
			filehandle.write(str(list2[i][j]) + " ")
		filehandle.write("\n")
	filehandle.close()

solutionlist = []

while(True):
	print("====SELECT====")
	print("[1]new game")
	print("[2]load game")
	print("[3]exit")
	select = input("what do you want? ")
	if select == "1":
		print("you selected new game")
		while(True):
			print("===select difficulty===")
			print("[1]easy")
			print("[2]medium")
			print("[3]hard")
			print("[4]exit")
			select = input("what do you want? ")
			if select == "1":
				formlist = []
				originallist = []
				setsheet("form//easy.txt")
				setsheet2("form//easy.txt")
				while(True):
					sheet(formlist)
					print("the format should be x<space>y<space>value")
					print("[a] exit game")
					print("[b] save game")
					a = input("input: ")
					if len(a) > 1:
						aa = a.split(" ")
						try:
							if (int(aa[0]) >= 1 and int(aa[0]) <= 9) and (int(aa[1]) >= 1 and int(aa[1]) <= 9) and (int(aa[2]) >= 1 and int(aa[2]) <= 9):
								if type(formlist[int(aa[0])][int(aa[1])]) == int:
									print("uneditable")
								else:
									formlist[int(aa[0])][int(aa[1])] = aa[2]
									checklist = convertint(formlist)
									if checking(checklist) == True:
										print("you solved the puzzle!")
										break
							else:
								print("invalid input")
						except:
							print("invalid input")
					if a == "b":
						save(formlist,originallist)
						print("progress saved!")
						break
					if a == "a":
						break
			if select == "2":
				formlist = []
				originallist = []
				setsheet("form//medium.txt")
				setsheet2("form//medium.txt")
				while(True):
					sheet(formlist)
					print("the format should be x<space>y<space>value")
					print("[a] exit game")
					print("[b] save game")
					a = input("input: ")
					if len(a) > 1:
						aa = a.split(" ")
						try:
							if (int(aa[0]) >= 1 and int(aa[0]) <= 9) and (int(aa[1]) >= 1 and int(aa[1]) <= 9) and (int(aa[2]) >= 1 and int(aa[2]) <= 9):
								if type(formlist[int(aa[0])][int(aa[1])]) == int:
									print("uneditable")
								else:
									formlist[int(aa[0])][int(aa[1])] = aa[2]
									checklist = convertint(formlist)
									if checking(checklist) == True:
										print("you solved the puzzle!")
										break
							else:
								print("invalid input")
						except:
							print("invalid input")
					if a == "b":
						save(formlist,originallist)
						print("progress saved!")
						break
					if a == "a":
						break
			if select == "3":
				formlist = []
				originallist = []
				setsheet("form//hard.txt")
				setsheet2("form//hard.txt")
				while(True):
					sheet(formlist)
					print("the format should be x<space>y<space>value")
					print("[a] exit game")
					print("[b] save game")
					a = input("input: ")
					if len(a) > 1:
						aa = a.split(" ")
						try:
							if (int(aa[0]) >= 1 and int(aa[0]) <= 9) and (int(aa[1]) >= 1 and int(aa[1]) <= 9) and (int(aa[2]) >= 1 and int(aa[2]) <= 9):
								if type(formlist[int(aa[0])][int(aa[1])]) == int:
									print("uneditable")
								else:
									formlist[int(aa[0])][int(aa[1])] = aa[2]
									checklist = convertint(formlist)
									if checking(checklist) == True:
										print("you solved the puzzle!")
										break
							else:
								print("invalid input")
						except:
							print("invalid input")
					if a == "b":
						save(formlist,originallist)
						print("progress saved!")
						break
					if a == "a":
						break
			if select == "4":
				break
	if select == "2":
		formlist = []
		loadsetsheet("form//save.txt","form//savecompare.txt")
		while(True):
			sheet(formlist)
			print("the format should be x<space>y<space>value")
			print("[a] exit game")
			print("[b] save game")
			a = input("input: ")
			if len(a) > 1:
				aa = a.split(" ")
				try:
					if (int(aa[0]) >= 1 and int(aa[0]) <= 9) and (int(aa[1]) >= 1 and int(aa[1]) <= 9) and (int(aa[2]) >= 1 and int(aa[2]) <= 9):
						if type(formlist[int(aa[0])][int(aa[1])]) == int:
							print("uneditable")
						else:
							formlist[int(aa[0])][int(aa[1])] = aa[2]
							checklist = convertint(formlist)
							if checking(checklist) == True:
								print("you solved the puzzle!")
								break
					else:
						print("invalid input")
				except:
					print("invalid input")
			if a == "b":
				save(formlist,originallist)
				print("progress saved!")
				break
			if a == "a":
				break
	if select == "3":
		break
