import os
import shutil

formats = {
    '音频':['.mp3','.wav'],
    '视频':['.mp4','.avi','.mov'],
    '图片':['.jpg','.png','.gif','.bmp','.jpeg'],
    '文档':['.doc','.xls','.docx','.pdf','.txt'],
    '程序':['.exe','.msi','.apk'],
    '压缩':['.zip','.rar','.7z'],
    '其它':[]
}

filenames = ['音频','视频','图片','文档','程序','压缩','其它']

#切换目录
os.chdir(r'C:\Users\MECHREVO\Downloads')


# f遍历文件夹，获取文件名称，ext取扩展名并转换为小写
for f in os.listdir():
    ext = os.path.splitext(f)[-1].lower()

#       
    for d,exts in formats.items():
        if not os.path.isdir(d):
            os.mkdir(d)
        if ext in exts:
            shutil.move(f,'{0}/{1}'.format(d,f))

for a in os.listdir():
    #b = os.path.splitext(a)[-1].lower()
    if a not in filenames:
        shutil.move(a,'其它/')


print('整理完成！')
