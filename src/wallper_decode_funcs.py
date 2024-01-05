import os
import datetime
import shutil
import json
import glob
import subprocess
from PIL import Image, ImageSequence
import re

# 解压pkg
def decode_pkg(repkg_path, src_dir):
    # 获取源目录下所有的.pkg文件
    pkgs = glob.glob(src_dir + '/' + '*.pkg')
    for pkg in pkgs:
        # repkg='./RePKG.exe'
        # 调用repkg
        cmd = ' '.join([repkg_path, 'extract', '"' +
                       pkg+'"', '-o', '"'+pkg[0:-4]+'"'])
        # print(cmd)
        subprocess.run(cmd)
        print('finish : ' + pkg)

# 处理目录下所有的gif
def decode_gif(src_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            # 获取文件的扩展名
            extension = os.path.splitext(file)[1].lower()
            if extension in ['.gif']:
                file_path = os.path.join(root, file)
                gif_to_grid(file_path)


# gif 转 宫格图.png （默认同一目录下，同名）
def gif_to_grid(gif):
    if os.path.exists(gif[0:-4]+'.png'):
        print(gif[0:-4]+'.png' +' exist, so skip')
        return 
    im = Image.open(gif)
    images = [frame.copy() for frame in ImageSequence.Iterator(im)]
    if len(images) == 0:
        return None

    # 获取每张图片的宽度和高度
    widths, heights = zip(*(img.size for img in images))

    # 计算宫格图的行列数
    cols = int(len(images) ** 0.5)
    rows = cols if cols * cols == len(images) else cols + 1

    max_width = max(widths)
    max_height = max(heights)

    # 计算宫格图的总宽度和总高度
    total_width = max_width * cols
    total_height = max_height * rows

    # 创建空白宫格图
    grid_image = Image.new('RGB', (total_width, total_height))

    # 将每张图片拼接到宫格图中
    for i, image in enumerate(images):
        x = (i % cols) * max_width
        y = (i // cols) * max_height
        grid_image.paste(image, (x, y))

    if grid_image is not None:
        grid_image.save(gif[0:-4]+'.png')
        print('gif to grid finish ' + gif[0:-4]+'.png')


def title(file_path):
    # 读取JSON文件
    with open(file_path, 'r', encoding='utf-8') as file:
        json_data = json.load(file)

    # 获取"title"关键字的值
    title = json_data["title"]
    # 定义不允许在Windows目录中出现的字符
    invalid_chars = r'[<>:"/\\|?*\x00-\x1F]'
    # 使用正则表达式替换掉不允许的字符
    cleaned_title = re.sub(invalid_chars, '', title)
    
    return cleaned_title.strip()


# 目录下'.jpg', '.png', '.gif', '.mp4'文件拷贝到目标目录，同名则覆盖
def imgs_to_dest(src, dest):
    if not os.path.exists(os.path.join(src,'project.json')):
        print(src + ' not have project.json , so skip.')
    target = title(os.path.join(src,'project.json'))
    for root, dirs, files in os.walk(src):
        for file in files:
            # 获取文件的扩展名
            extension = os.path.splitext(file)[1].lower()
            if extension in ['.jpg', '.png', '.gif', '.mp4', '.mp3']:
                file_path = os.path.join(root, file)
                # 创建目标文件夹的父目录
                os.makedirs(os.path.join(dest, target), exist_ok=True)
                # 拷贝文件到指定文件夹
                # print('dest : ' + os.path.join(dest, os.path.basename(src), file))
                if os.path.exists(os.path.join(dest,target,file)):
                    print(os.path.join(dest,target,file) + ' exist, so skip')
                else:
                    shutil.copy(file_path, os.path.join(dest,target,file))
    print(target + ' is ok')
 

def clean(src_dir):
    # 获取源目录下所有的.pkg文件
    pkgs = glob.glob(src_dir + '/' + '*.pkg')
    for pkg in pkgs:
        # 删除解压的目录
        shutil.rmtree(pkg[0:-4])
    if os.path.exists(src_dir+'/preview.png'):
        os.remove(src_dir+'/preview.png')