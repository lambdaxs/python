#coding=utf-8
import os
import platform


#改后缀，修改文件名，
# path = 'c://dir//'
# path = '/Users/xiaos/dir/'
supPath = '/Users/xiaos/Desktop/video/javaWeb/'
# path = '/Users/xiaos/Desktop/video/javaWeb/01-Java基础增强/'

hrefStr = '_helloworld_'
osList = ['Lunix','Darwin','Ubuntu']
# lastStr = 'xxx'

#新建同类型测试文件
def setUpFiles(path,hrefStr):
	
	list = []
	for i in range(10):
		list.append(path+hrefStr+'b%s.txt' %(i))

	for i in range(10):
		f = open(list[i],'w')
		f.close()

	print("在"+path+"目录下生成了测试文件")


def dirName(supPath):
	list = os.listdir(supPath)
	if(platform.system() in osList):
		del list[0]
	return list

pathList = dirName(supPath)[2:-1]

#返回path目录下的文件全名
def filesAllName(path):
	list = os.listdir(path)
	if(platform.system() in osList):
		del list[0]
		
	return list

#返回一个数组，保存每次操作前的文件名

#替换文件名中指定的字符串
def replaceStr(path,oldStr,newStr):
	newName = []
	oldName = filesAllName(path)
	j = 0
	for i in filesName(path):
		newName.append(i.split(oldStr)[0]+newStr+i.split(oldStr)[1]+'.'+filesType(path)[j])
		j = j + 1

	for i in range(len(newName)):
		os.rename(path+oldName[i], path+newName[i])

	print("成功替换名称！")





#去掉文件类型后缀，返回文件名称
def filesName(path):
	tmp = []
	list = filesAllName(path)
	for i in list:
		i = i.split('.')[0]
		tmp.append(i)
	return tmp

#返回文件类型
def filesType(path):
	tmp = []
	list = filesAllName(path)
	for i in range(len(list)):
		tmp.append(list[i].split('.')[1])
	return tmp

#统一添加文件名后缀
def addStr(path,lastStr):
	newName = []
	oldName = filesAllName(path)
	j = 0
	for i in filesName(path):
		newName.append(i+lastStr+'.'+filesType(path)[j])
		j = j + 1

	for i in range(len(newName)):
		os.rename(path+oldName[i], path+newName[i])

	print("成功添加后缀！")

#统一添加文件名前缀
def addFirstStr(path,firstStr):
	newName = []
	oldName = filesAllName(path)
	j = 0
	for i in filesName(path):
		newName.append(firstStr+i+'.'+filesType(path)[j])
		j = j + 1

	for i in range(len(newName)):
		os.rename(path+oldName[i], path+newName[i])

	print("成功添加前缀！")

#统一修改文件名后缀
def addFilesType(path,filesType):
	newName = []
	oldName = filesAllName(path)
	for i in filesName(path):
		newName.append(i+'.'+filesType)

	for i in range(len(newName)):
		os.rename(path+oldName[i], path+newName[i])

	print("成功修改文件类型！")


# setUpFiles(path, hrefStr) 

# addFilesType(path,'png')

# addFirstStr(path, '')


# addStr(path,'hh')
# for i in pathList:
# 	path = supPath+i+'/'
# 	replaceStr(path,'_黑马程序员_', '_')

# replaceStr(path, '_黑马程序员_', '_')

# print(os.listdir(path))
