#coding=utf-8
import os


#改后缀，修改文件名，
path = '/Users/xiaos/dir/'
hrefStr = '_helloworld_'
# lastStr = 'xxx'

#新建同类型测试文件
def setUpFiles(path,hrefStr):
	
	list = []
	for i in range(10):
		list.append(path+hrefStr+'b%s.txt' %(i))

	for i in xrange(10):
		f = open(list[i],'w')
		f.close()


#返回path目录下的文件全名
def filesAllName(path):
	list = os.listdir(path)
	del list[0]
	return list

#去掉文件后缀，返回文件名称
def filesName(path):
	tmp = []
	list = filesAllName(path)
	for i in list:
		i = i.split('.')[0]
		tmp.append(i)
	return tmp

#返回文件类型
def filesType(path):
	list = filesAllName(path)
	tmp = list[0].split('.')[1]
	return tmp

#统一添加文件名后缀
def addStr(path,lastStr):
	newName = []
	for i in filesName(path):
		newName.append(i+lastStr+'.'+filesType(path))

	for i in range(len(newName)):
		os.rename(path+filesAllName(path)[i], path+newName[i])


#统一添加文件名后缀
def addFilesType(path,filesType):
	newName = []
	for i in filesName(path):
		newName.append(i+'.'+filesType)

	for i in range(len(newName)):
		os.rename(path+filesAllName(path)[i], path+newName[i])


addFilesType(path,'png')
# #统一添加文件名前缀
# def addFirstStr(path,firstStr):
# 	newName = []
# 	for i in filesName(path):
# 		newName.append(firstStr+i+'.'+filesType(path))

# 	for i in range(len(newName)):
# 		print(path+filesAllName(path)[i])
# 		print(path+newName[i])
# 		os.rename(path+filesAllName(path)[i], path+newName[i])

# 	print('前缀添加成功！')


# addFirstStr(path, 'first_')

# addFirstStr(path,'xx')
# addStr(path,'hh')
# setUpFiles(path, hrefStr)
# print(os.listdir(path))
