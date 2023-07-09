import wallper_decode_funcs as funcs

# 1、输入：给定一个目录列表+RePkg目录，输出：将每个目录解析的结构放到，目标目录
# 2、对每一个目录进行单独解析
# 2.1、解压scene.pkg到当前目录下的scene文件夹
# 2.2、为每个gif文件创建同名的.png宫格图文件
# 2.3、将目录下所有的 jpg png gif mp4 拷贝到目标目录
# 2.4、删除scene文件夹

def solve(repkg, dir):
    funcs.decode_pkg(repkg, dir)
    funcs.decode_gif(dir)


def copyTo(dir, dest_dir):
    funcs.imgs_to_dest(dir, dest_dir)
    funcs.clean(dir)

dirs = [
    'xxx\Steam\steamapps\workshop\content/431960/2932511679'
]
dest_dir = 'xxxx'
# https://github.com/notscuffed/repkg
repkg = 'xxxx/RePKG.exe'

for dir in dirs:
    solve(repkg, dir)
    copyTo(dir, dest_dir)
