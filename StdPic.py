
# section of importing modules
#############################################################
import time   # 计算前后总共花费的运行时间用。以及sleep延迟用。

from argparse import ArgumentParser # 用于过滤命令行上的参数选项。

import os.path                      # 用于文件是否存在的判断。

import os                           # 用于检查文件的尺寸大小。

import sys                          # 当前代码行号的显示，要用到。

import configparser                 # 用来读配置文件

from pathlib import Path            # 测试是否存在路径或文件。

import logging                      # 做日志记录的手段

# import numpy as np                  # 做jpg文件大小的读取

# try:
    # import cv2
# except ImportError:
    # print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       # "试图加载模块时失败，再试: opencv-python\n")
    # os.system('python -m pip install opencv-python')

# import cv2                          # 做jpg文件大小的读取



try:
    import PIL
except ImportError:
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " 试图加载模块时失败，再试: pillow\n")
    os.system('python -m pip install pillow')

from PIL import Image               # 读取jpg文件的大小。
   
from random import choice           # 生成随机字串

from string import ascii_uppercase  # 生成字串范围

import shutil                       # 拷贝文件要用到。

try:                                # 这个模块用于获得windows的路径。
    import winshell
except ImportError:
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " 试图加载模块时失败，再试: winshell \n")
    os.system('python -m pip install winshell')

import winshell
    
from win32com.client import Dispatch  # 创建快捷方式要用到。

import string                         # 创建随机字符串要用到。

## strTemp = input("请按任意键继续")

# pip install numpy
# pip install opencv-python
# pip install pillow

# section of sub routines
#############################################################

# the main routine of this script
#############################################################


# Test print("Hello")

# 1. 读取命令行参数
# 2. 读取配置文件
# 3. 建立日志系统
# 4. 读取源图片文件的参数
# 5. 判断是取高还是取宽
# 6. 进行依高或依宽的resize
# 7. 进行crop
# 8. 验证新图片wxh符合要求，并取得quality参数
# 9. 按图片文件大小的要求，逐步试压缩quality
# 10. 验证目标图片文件的大小，符合要求，予以存放。

# 0. 版权页信息

strAppVersion = "V 1.0.3"
strAppHomepage = "https://github.com/evering7/StandardizePicture"
print("制作考试用的标准证件照 by Python 版本号：" + strAppVersion)
print("项目主页：" + strAppHomepage)
print("作者：福建莆田 李剑飞 13799001059@139.com")
print("代码的最后修改日期：2019.4.20")
time.sleep(1)  # 停留一会儿。


# 1. 读取命令行参数
#############################################################
# 1.1. 检查命令行参数，有一个命令，一个参数。
# 1.2. 文件参数必须存在，否则报错退出。

# def is_valid_file(parser, arg):
    # if not os.path.exists(arg):
        # parser.error("文件 %s 不存在!" % arg)
    # else:
        # return open(arg, 'r')  # return an open file handle
        # # return

# parserArgs = ArgumentParser(description='一键自动生成标准身份证照。')

# parserArgs.add_argument("-i", dest="strSrcPicFilePath_FromCmdLine", required=True,
                    # help="请指出待标准化的源照片", metavar="源图像的文件路径名",
                    # type=lambda x: is_valid_file(parserArgs, x))

# parserArgs.print_help()
                    
# args = parserArgs.parse_args()

# print(sys.argv[1:])
## strTemp = input()


# 此处需要改写，改成能容纳多个文件的样子。
sourceFiles = sys.argv[1:]

# 此处：如果没有一个源文件，那么就建立快捷方式。
if len(sourceFiles) == 0:
    # 此处：建立快捷方式。
    strSendToFolder = winshell.sendto()
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " 取得发送到文件夹的全路径名 = " + strSendToFolder)
       
    # 准备创建快捷方式
    shell = Dispatch('WScript.Shell')
    strStdPic_CmdFullPath = os.path.splitext(os.path.realpath(__file__))[0] + ".cmd"
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " Command脚本文件的全路径 = " + strStdPic_CmdFullPath)
    
    strRandom = ''.join(choice(string.ascii_letters + string.digits ) for i in range(8))
    strShortCut_Location = strSendToFolder + "\\转换图片成为标准照-" + strRandom + ".lnk"  
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " 快捷方式的存放路径 = " + strShortCut_Location)
    
    # strTemp = input("请按回车键继续：")
    shortcut = shell.CreateShortCut(strShortCut_Location)
    shortcut.Targetpath = strStdPic_CmdFullPath
    
    strScriptContainingFolder = os.path.dirname(__file__)
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " 快捷方式的工作目录 = " + strScriptContainingFolder)
       
    shortcut.WorkingDirectory = strScriptContainingFolder
    
    icon_Path = strScriptContainingFolder + "\\2754580 - avatar business face people.ico"
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
       " 图标文件的路径 = " + icon_Path)
    
    shortcut.IconLocation = icon_Path
    shortcut.save()
    
    # strTemp = input("完成发送到的快捷方式设置，请按回车键退出：")
    
    
    quit()
    # import os, winshell
    # from win32com.client import Dispatch
     
    # desktop = winshell.desktop()
    # path = os.path.join(desktop, "Media Player Classic.lnk")
    # target = r"P:\Media\Media Player Classic\mplayerc.exe"
    # wDir = r"P:\Media\Media Player Classic"
    # icon = r"P:\Media\Media Player Classic\mplayerc.exe"
     
    # shell = Dispatch('WScript.Shell')
    # shortcut = shell.CreateShortCut(path)
    # shortcut.Targetpath = target
    # shortcut.WorkingDirectory = wDir
    # shortcut.IconLocation = icon
    # shortcut.save()
    
    
    
existSourceFiles = []


#bAllNotExist = True
for iFile in range(len(sourceFiles)):
    # 开始循环检查
    currentFile = Path(sourceFiles[iFile])
    if currentFile.is_file() and os.path.exists(sourceFiles[iFile]):
        # bAllNotExist = False
        print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
           " 文件存在 " + sourceFiles[iFile])
        existSourceFiles += [sourceFiles[iFile]]
    else:
        print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
           " 文件不存在！！ " + sourceFiles[iFile])
    
    # myFile = Path(MyBookProject_IniPath)
    # if myFile.is_file():
        # print("file exist!")
        # #return True
    # else:
        # print("file non exist")     # # if (not ifFileExist(MyBookProject_IniPath)):
        # print("所要的ini文件不存在")
        # quit()
        
print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
    " 真正存在的文件列表：" + str(existSourceFiles))

if len(existSourceFiles) == 0 :
    print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
        "所输入的文件参数均不存在，退出。")
    ## strTemp = input()
    quit()

# quit()

# Test print(args)

# Test print(args.strSrcPicFilePath_FromCmdLine)

# Test print(args.strSrcPicFilePath_FromCmdLine.name)

# 下面取得源文件的全路径名。
## strSourcePicture_FullPath = args.strSrcPicFilePath_FromCmdLine.name

## args.strSrcPicFilePath_FromCmdLine.close()  # 进行关闭操作。

## print(time.strftime('%Y%m%d_%H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " 当前源文件的全路径是：" + strSourcePicture_FullPath)

# 判断源图像文件存在与否。
# # mySrcPicFile = Path(strSourcePicture_FullPath)
# # if mySrcPicFile.is_file():
    # # print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " 源图像文件存在，文件全名 = " + strSourcePicture_FullPath)    
# # else:
    # # print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " 源图像文件不存在。文件全名 = " + strSourcePicture_FullPath)     # # if (not ifFileExist(MyBookProject_IniPath)):
    # # # print("所要的ini文件不存在")
    # # time.sleep(7)
    # # quit()

# 2. 读取配置文件
#############################################################
# 接下来，读取配置文件。
# 2.1. 日志文件的前缀名
# 2.2. 日志文件的存放目录
# 2.3. 目标图像宽度
# 2.4. 目标图像高度
# 2.5. 目标图像的文件大小上限。
# 2.6. 各种程序文件的全路径位置
# 2.7. 要遍历ini中的所有配置，列举出来供用户选择。然后读取以上信息。

# 1. 先获取脚本文件的目录所在地。
strDirPath_ofCurrentScript = os.path.dirname(os.path.realpath(__file__))
strBareName_ofCurrentScript = os.path.splitext(os.path.realpath(__file__))[0]
# os.path.splitext("path_to_file")[0])
print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " 当前脚本所在的目录是：" + strDirPath_ofCurrentScript)

# 2. 寻找文件夹下的.ini
MyStdPicProject_IniPath =  strBareName_ofCurrentScript + ".ini"

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " 当前脚本所对应的ini文件为：" + MyStdPicProject_IniPath)

# 3. 验证文件是否存在。
myIniFile = Path(MyStdPicProject_IniPath)
if myIniFile.is_file():
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " Ini配置文件存在，文件全名 = " + MyStdPicProject_IniPath)    
else:
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + " Ini配置文件不存在。文件全名 = " + MyStdPicProject_IniPath)     # # if (not ifFileExist(MyBookProject_IniPath)):
    # print("所要的ini文件不存在")
    quit()

# 4. 已经验证文件存在。
# 那么就开始读取ini文件中的数据，首要的是设定当前的主节号 Section Name。
IniConfig = configparser.ConfigParser()
IniConfig.read(MyStdPicProject_IniPath, encoding='utf8')

# 4.b. 此处插进文字，准备选ini的字段
listOfSections = IniConfig.sections()

print("请选择如下目标格式的其中一项：")

for i in range(len(listOfSections)):
    print(" " + str(i + 1) + " " + listOfSections[i])

print(" " + str(len(listOfSections)+1) + " 新增一个转换相片标准的类别" )    
# print("请输入你想要的索引项：")
# time.sleep(10)

# 4.c2. 此处调整参数的名字
strStdPicItemName_LogFileNamePrefix = "LogFileNamePrefix"
strStdPicItemName_LogFolder = "LogFolder"
strStdPicItemName_TempFolder = "TempFolder"
strStdPicItemName_DestPicWidth = "DestPicWidth"
strStdPicItemName_DestPicHeight = "DestPicHeight"
strStdPicItemName_DestPicFileSize_UpBound = "DestPicFileSize_UpBound_inK"


# LogFileNamePrefix=StandardizePersonPicture.cpa2019
# LogFolder=StdPicLogs2
# TempFolder=TempFolder2
# DestPicWidth=358
# DestPicHeight=441
# DestPicFileSize_UpBound_inK=10

# 4.c. 此处放进输入函数。




userSelectSectionIndexStr = input("请输入你想要的转换项目：")

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 用户所取得的索引 = " + userSelectSectionIndexStr) 

userSelectSectionIndex = int(userSelectSectionIndexStr)

# myTrickIndex = -1

if (userSelectSectionIndex <= 0 or userSelectSectionIndex > (1+len(listOfSections))):
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
        "用户的选择有误，所输入的项索引号，应当大于0，小于等于" + str(len(listOfSections)))
    quit()
elif userSelectSectionIndex == (1 + len(listOfSections)):
    
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
        " 用户的选择：新建一个转换标准，所输入的项索引号 = " + str(1 + len(listOfSections)))
    # 此处加上处理的子例程。
    nNewSectionName = input("请输入新的照片转换项目名称：")
    if len(nNewSectionName) == 0:
        print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 照片文件的转换项目名称为空字符串。退出。")
        quit()    
    
    nNewDestPicWidth = int(input("请输入照片文件的目标宽度（以像素为单位）："))
    if nNewDestPicWidth <= 0 :
        print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 照片文件的目标宽度不能小于等于零。退出。")
        quit()
    
    nNewDestPicHeight = int(input("请输入照片文件的目标高度（以像素为单位）："))
    if nNewDestPicHeight <= 0 :
        print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 照片文件的目标高度不能小于等于零。退出。")
        quit()
    
    kNewDestPicFileSize_UpBound = int(input("请输入照片文件的目标尺寸上限（以K为单位，如30K，只要输入30）："))
    if kNewDestPicFileSize_UpBound <= 0 :
        print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 照片文件的目标尺寸不能小于等于零。退出。")
        quit()    
    
    # 获取上述目标尺寸信息后，开始写入ini文件的操作。
    
    
    IniConfig.add_section(nNewSectionName)
    IniConfig.set(nNewSectionName, strStdPicItemName_LogFileNamePrefix , nNewSectionName ) # 此项用户不需要输入
    IniConfig.set(nNewSectionName, strStdPicItemName_LogFolder , "StdPicLogs")             # 此项用户不需要输入
    IniConfig.set(nNewSectionName, strStdPicItemName_TempFolder, "TempFiles")              # 此项用户不需要输入
    
    IniConfig.set(nNewSectionName, strStdPicItemName_DestPicWidth, str(nNewDestPicWidth))  # 输入宽度
    IniConfig.set(nNewSectionName, strStdPicItemName_DestPicHeight, str(nNewDestPicHeight))# 输入高度
    IniConfig.set(nNewSectionName, strStdPicItemName_DestPicFileSize_UpBound, str(kNewDestPicFileSize_UpBound)) # 输入大小的上限
    
    # IniConfig.write(MyStdPicProject_IniPath)
    with open(MyStdPicProject_IniPath, mode = 'w', encoding="utf8") as configfile:
        IniConfig.write(configfile)
    
    # 写完后，不必问是否继续录入新的项目
    print(time.strftime('%Y%m%d %H%M%S', time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 已经完成新项目的录入，程序马上按新项目进行转换。如果用户需要批量录入新项目，请直接编辑.ini配置文件 " + MyStdPicProject_IniPath)
    
    
        
    ## quit()

# with open('test_update.ini', 'w') as configfile:
    # config.write(configfile)
    
# DestPicWidth=358
# DestPicHeight=441
# DestPicFileSize_UpBound_inK=10
    
# parser.add_section('bug_tracker')
# parser.set('bug_tracker', 'url', 'http://localhost:8080/bugs')
# parser.set('bug_tracker', 'username', 'dhellmann')
# parser.set('bug_tracker', 'password', 'secret')

listOfSections = IniConfig.sections() # 重新刷新一遍，

strCurrentSectionName = listOfSections[userSelectSectionIndex - 1]
    
time.sleep(4)

# strCurrentSectionName = "注会2019"

# 2.1. 日志文件的前缀名
# 2.2. 日志文件的存放目录
# 2.3. 目标图像宽度
# 2.4. 目标图像高度
# 2.5. 目标图像的文件大小上限。
# 2.6. 各种程序文件的全路径位置

strLogFileNamePrefix = IniConfig.get(strCurrentSectionName,'LogFileNamePrefix')  # 此句放此处，用来检视

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 日志文件名的前缀 = " + strLogFileNamePrefix) 

strLogFolder = IniConfig.get(strCurrentSectionName, 'LogFolder')

if strLogFolder[1] == ':':
    # 维持路径名不变
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
        " 日志文件的存放文件名含有冒号，作绝对路径理解 = " + strLogFolder)
else:
    strLogFolder = os.path.dirname(__file__) + "\\" + strLogFolder
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
        " 日志文件的存放文件夹，用了相对路径，现展为全路径 = " + strLogFolder)

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 日志文件的存放文件夹 = " + strLogFolder) 

## quit()
     
# 以上是日志文件的存放文件夹，要测试文件夹是否存在，不存在则建立之。
if not os.path.exists(strLogFolder):
    os.makedirs(strLogFolder)
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 创建存放日志的文件夹 = " + strLogFolder)

# strLogFolder  strLogFileNamePrefix

def getFullPath_WithAbsOrRelString(strTempPathString):
    # 这个函数把相对路径绝对化。
    if strTempPathString[1] == ':':
    # 维持路径名不变
        print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 存放文件夹名含有冒号，作绝对路径理解 = " + strTempPathString)
        return strTempPathString
    else:
        strTempPathString = os.path.dirname(__file__) + "\\" + strTempPathString
        print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
            " 存放文件夹用了相对路径，现展为全路径 = " + strTempPathString)
        return strTempPathString
        
# 2.2b. 临时文件的全路径名。TempFolder
strTempFolder = IniConfig.get(strCurrentSectionName, 'TempFolder')

strTempFolder = getFullPath_WithAbsOrRelString(strTempFolder)

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 临时文件的存放文件夹 = " + strTempFolder) 

# 以上是日志文件的存放文件夹，要测试文件夹是否存在，不存在则建立之。
if not os.path.exists(strTempFolder):
    os.makedirs(strTempFolder)
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 创建存放临时文件的文件夹 = " + strTempFolder)
	 
# quit()

# 2.3. 目标图像宽度
nDestPicWidth =  int(IniConfig.get(strCurrentSectionName, 'DestPicWidth'))
print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 图像的目标宽度 = " + str(nDestPicWidth)) 

# 2.4. 图像的目标高度
nDestPicHeight =  int(IniConfig.get(strCurrentSectionName, 'DestPicHeight'))
print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 图像的目标高度 = " + str(nDestPicHeight)) 

# 2.5. 图像文件尺寸的目标上限
nDestPicFileSize_UpBound_inK = int(IniConfig.get(strCurrentSectionName, 'DestPicFileSize_UpBound_inK'))
nDestPicFileSize_UpBound_Byte = nDestPicFileSize_UpBound_inK * 1000

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     " 图像文件尺寸的目标上限（以K为单位） = " + str(nDestPicFileSize_UpBound_Byte))

# # 2.6. 程序文件的全路径位置
# strMagickCmd_FullPath = IniConfig.get(strCurrentSectionName, 'MagickExe_FullPath')
# print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
     # " 程序文件的全路径位置 = " + strMagickCmd_FullPath)

# # 2.6.b 判断该程序文件是否存在。
# myMagickCmdFile = Path(strMagickCmd_FullPath)
# if myMagickCmdFile.is_file():
    # print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
    # " ImageMagick执行文件存在 = " + strMagickCmd_FullPath)    
# else:
    # print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
    # " ImageMagick执行文件不存在。文件全名 = " + strMagickCmd_FullPath)     # # if (not ifFileExist(MyBookProject_IniPath)):
    # # print("所要的ini文件不存在")
    # quit()
     


# 3. 建立日志系统
#############################################################
# 开始建立日志系统 2019.4.16
# Create the Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create the Handler for logging data to a file
# 此处，需要改名字，把日期时间嵌进文件名。
# 以下这句用了两处地方。
strFixedTime = time.strftime('%Y%m%d_%H%M%S',time.localtime())

# strLogFileName = "E:\\mydoc\\20180607 准备出书的文件\\00_Round_1_Volume_3_EcoFinance\\Logs\\PyMake_Vol_3_" + strFixedTime + '.log'

strLogFileName = strLogFolder + "\\" + strLogFileNamePrefix + "_" + strCurrentSectionName + "_" + strFixedTime + '.log'

print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(sys._getframe().f_lineno) + \
 " 当前的日志文件全路径名 = " + strLogFileName)

# quit()

logger_handler = logging.FileHandler(strLogFileName)
logger_handler.setLevel(logging.DEBUG)


# 创设一个格式
logger_formatter = logging.Formatter('%(asctime)s %(name)s - %(levelname)s - %(message)s')

# Add the Formatter to the Handler
logger_handler.setFormatter(logger_formatter)

# Add the Handler to the Logger
logger.addHandler(logger_handler)
# logger.info("行号 " + str(sys._getframe().f_lineno) + 'Completed configuring logger()!')
logger.info("行号 " + str(sys._getframe().f_lineno) + ' 完成日志文件的配置')

## strTemp = input()

# 增加一个打印日志的函数。
###############################################################      子程序模块

def print_log(line_number, strPrint):  # 这个子程序做到tee输出，一面向日志，一面向终端。
    logger.info("行号 " + str(line_number) + " " + strPrint)
    print(time.strftime('%Y%m%d %H%M%S',time.localtime()) + " 行号 " + str(line_number) + " " + strPrint)

# 4. 读取源图片文件的参数
#############################################################
# img = cv2.imread(strSourcePicture_FullPath)
# # imgHeight, imgWidth, imgChannels = img.shape
# imgHeight = np.size(img,0)
# imgWidth  = np.size(img,1)

def imageProcess(strSourcePicture_FullPath):
    img = Image.open(strSourcePicture_FullPath)

    (imgWidth, imgHeight) = img.size

    print_log(sys._getframe().f_lineno, "当前图像的宽度x高度 = " + str(imgWidth) + " x " + str(imgHeight))

    # 5. 判断是取高还是取宽
    #############################################################
    # 开始进行取高还是取宽的操作。

    srcImage_WidthHeightRatio = imgWidth / imgHeight
    destImage_WidthHeightRatio = nDestPicWidth / nDestPicHeight

    print_log(sys._getframe().f_lineno, "源图像的宽除以高比例 = " + str(srcImage_WidthHeightRatio))

    print_log(sys._getframe().f_lineno, "目标图像的宽除以高比例 = " + str(destImage_WidthHeightRatio))

    # 源 0.7 目标 0.8
    # 源高大一点，宽与目标同宽

    resizeImage_Width = 100
    resizeImage_Height = 200

    if srcImage_WidthHeightRatio > destImage_WidthHeightRatio:
        # 如果源0.8 目标 0.6 ，那么源的宽向要缩窄。
        print_log(sys._getframe().f_lineno, "源宽/源高 > 终宽/终高，正在试验处理。")
        resizeImage_Height = nDestPicHeight
        resizeImage_Width = int(nDestPicHeight * srcImage_WidthHeightRatio)
        # quit()
    else:
        resizeImage_Width = nDestPicWidth
        resizeImage_Height = int(nDestPicWidth / srcImage_WidthHeightRatio)

    print_log(sys._getframe().f_lineno, "计算出来的目标图像实际 宽 x 高 = " + str(resizeImage_Width) + " x " + str(resizeImage_Height))


    # 6. 进行依高或依宽的resize
    #############################################################
    # 进行真正的resize
    # image = Image.open('unsplash_01.jpg')
    #image.thumbnail((400, 400))
    #image.save('image_thumbnail.jpg')

    # 6.1. 预先生成临时文件名


    strRandom = ''.join(choice(ascii_uppercase) for i in range(16))

    strTempResizeFile = strTempFolder + "\\" + time.strftime('%Y%m%d-%H%M%S',time.localtime()) + "-TempResize-" + strRandom + ".jpg"

    print_log(sys._getframe().f_lineno, "当前的临时随机图像路径为 " + strTempResizeFile)

    resize_image = img.resize((resizeImage_Width, resizeImage_Height))
    resize_image.save(strTempResizeFile)

    # 7. 进行crop
    #############################################################
    # 现在进行裁剪。样本代码如下。

    # image = Image.open('unsplash_01.jpg')
    # box = (150, 200, 600, 600)
    # cropped_image = image.crop(box)
    # cropped_image.save('cropped_image.jpg')
    UpLeftX = 0
    UpLeftY = 0
    DownRightX = 0
    DownRightY = 0

    if srcImage_WidthHeightRatio > destImage_WidthHeightRatio:
          # 源比目标更宽更胖
        UpleftY = 0
        UpLeftX = int((resizeImage_Width - nDestPicWidth) / 2)
        DownRightY = nDestPicHeight
        DownRightX = nDestPicWidth + UpLeftX
        
    else: # 源比目标更高更瘦
        UpLeftX = 0
        UpLeftY = int((resizeImage_Height - nDestPicHeight) / 2)
        DownRightX = nDestPicWidth
        DownRightY = int(nDestPicHeight + UpLeftY )

    cropBox = (UpLeftX, UpLeftY, DownRightX , DownRightY)
    print_log(sys._getframe().f_lineno, "要剪裁的盒子参数 左上角X 左上角Y 宽 高 = " + str(cropBox))

    cropped_image = resize_image.crop(cropBox)

    strRandom = ''.join(choice(ascii_uppercase) for i in range(16))
    strCropped_Image_File_FullPath = strTempFolder + "\\" + time.strftime('%Y%m%d-%H%M%S',time.localtime()) + "-TempCropped-" + strRandom + ".jpg"

    cropped_image.save(strCropped_Image_File_FullPath)

    # 8. 验证新图片wxh符合要求，并取得quality参数
    #############################################################
    #img = Image.open(strSourcePicture_FullPath)

    (cropImgWidth, cropImgHeight) = cropped_image.size

    print_log(sys._getframe().f_lineno, "裁剪后图像的宽度x高度 = " + str(cropImgWidth) + " x " + str(cropImgHeight))

    if (cropImgWidth != nDestPicWidth) or (cropImgHeight != nDestPicHeight):
        print_log(sys._getframe().f_lineno, "裁剪后的图像宽高，还是与目标框架尺寸不匹配。")
        time.sleep(10)
        #quit()

    # 9. 按图片文件大小的要求，逐步试压缩quality
    #############################################################
    #try:
        # = Image.open(os.path.join(root, name))
        #print "Converting jpeg for %s" % name
        #im.thumbnail(im.size)
    # 2019.4.17 要取得quality参数。    
    # 2019.4.18 要进行循环取数。

    qualityInLoop = 95

    while (qualityInLoop >= 25):
        # 开始压缩操作。    
        strRandom = ''.join(choice(ascii_uppercase) for i in range(16))
        strTempChangeQuality = strTempFolder + "\\" + time.strftime('%Y%m%d-%H%M%S',time.localtime()) + "-TempChangeQuality-" + str(qualityInLoop) + "-" + strRandom + ".jpg"
        print_log(sys._getframe().f_lineno, "当前的临时随机改变画质的图像路径为 " + strTempChangeQuality)
        cropped_image.save(strTempChangeQuality, "JPEG", quality=qualityInLoop)
        # 如果循环中发现所得结果文件尺寸大小小于规定的30000则退出循环。
        # nDestPicFileSize_UpBound_Byte
        fileStatInfo = os.stat(strTempChangeQuality)
        fileSize = fileStatInfo.st_size
        print_log(sys._getframe().f_lineno, "得到的文件尺寸大小 = " + str(fileSize))
        if fileSize < nDestPicFileSize_UpBound_Byte:
            print_log(sys._getframe().f_lineno, "文件尺寸已经小于给定的尺寸上限，退出循环。")
            break
        qualityInLoop -= 5

    # 这里要加名字了，存储最终的文件。
    strDestPathWithoutExtension = os.path.splitext(strSourcePicture_FullPath)[0] # 取得除扩展名之外的全路径名

    # 取得加长后的名字。
    strRandom = ''.join(choice(ascii_uppercase) for i in range(16))

    strDestFullPath = strDestPathWithoutExtension + "-" + strCurrentSectionName + "-" + strRandom + ".jpg"

    print_log(sys._getframe().f_lineno, "新取得的目标图片文件全路径名 = " + strDestFullPath )

    # strTemp = input()


    shutil.copyfile(strTempChangeQuality, strDestFullPath)  
    # 此处文件的处理结束。
    
for iExistFile in range(len(existSourceFiles)):
    imageProcess(existSourceFiles[iExistFile])

# strTemp = input()
# 1. 步骤：浏览 >> 上传 >> 剪切 >> 保存。
# 2. 截图照片必须为免冠正面照，截图时必须露出整个头部并且截到肩部，头像居于正中（见右侧示例图片）。源照片背景须为白色，格式为jpg，照片大于30kb小于100kb，250*350像素。
# 3. 该照片一旦审核通过不允许修改。报名表、准考证、执业资格证书等均使用该照片，如因使用美图、Photoshop等修图软件过度修饰照片导致无法正常参加考试等后果，由考生自行承担。

# strSourcePicture_FullPath

# strBareName_ofCurrentScript = os.path.splitext(os.path.realpath(__file__))[0]

# strCurrentSectionName

# >>> import os
# >>> statinfo = os.stat('somefile.txt')
# >>> statinfo
# (33188, 422511L, 769L, 1, 1032, 100, 926L, 1105022698,1105022732, 1105022732)
# >>> statinfo.st_size
# 926L

# E:\mydoc\20180607 准备出书的文件\Book_2_Round_2_Computer\bin_OneQualityPic\TempFolder>
# "D:\Program Files\ImageMagick-7.0.8-Q16\magick.exe" identify -verbose 20190416-221548-TempResize-BKDRVWLNYOYVCKJU.jpg

# except Exception, e:
    # print(e)
# 10. 验证目标图片文件的大小，符合要求，予以存放。
#############################################################
