
import os
import datetime
import wallper_decode_funcs as funcs
import shutil

def getFilesByTime(src_dir, limit):
    # 获取文件夹下的所有子文件夹
    subfolders = [f.path for f in os.scandir(src_dir) if f.is_dir()]

    # 按修改时间对子文件夹进行排序
    sorted_subfolders = sorted(
        subfolders, key=lambda x: os.path.getmtime(x), reverse=True)

    return sorted_subfolders[:limit]


def printFilesWithTime(dirs):
    # 打印排序后的子文件夹列表
    cnt=0
    for subfolder in dirs:
        cnt+=1
        target = funcs.title(os.path.join(subfolder,'project.json'))
        modified_time = os.path.getmtime(subfolder)
        modified_time_str = datetime.datetime.fromtimestamp(
            modified_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f'{cnt} : {target} (Modified Time: {modified_time_str})')


def printDirs(dirs):
    cnt=0
    for subfolder in dirs:
        cnt+=1
        modified_time = os.path.getmtime(subfolder)
        modified_time_str = datetime.datetime.fromtimestamp(
            modified_time).strftime('%Y-%m-%d %H:%M:%S')
        print(f'{cnt} : {subfolder} (Modified Time: {modified_time_str})')


def search(src_dir, str):
    # 获取文件夹下的所有子文件夹
    subfolders = [f.path for f in os.scandir(src_dir) if f.is_dir()]
    filtered_list = [x for x in subfolders if str in x]
    return filtered_list

def fuzzy_search_directory(directory, keyword):
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if keyword in file:
                file_paths.append(os.path.join(root, file))
    return file_paths


def batch_copy_files(source_directory, destination_directory):
    for root, dirs, files in os.walk(source_directory):
        for file in files:
            source_path = os.path.join(root, file)
            destination_path = os.path.join(destination_directory, file)
            shutil.copy2(source_path, destination_path)


def copy_file(source_file_path, destination_directory):
    shutil.copy2(source_file_path, destination_directory)


# 指定目录和关键字进行模糊查找
# directory = "E:/night/0910/0507_view"  # 替换为你要查找的目录路径
# directory1 = "E:/night/HongKongDoll"  # 替换为你要查找的目录路径
directory1 = "D:/game/steam/Steam/steamapps/workshop/content/431960/2955676529"  # 替换为你要查找的目录路径
# keyword = "HongKongDoll"  # 替换为你要模糊匹配的关键字
# found_files = fuzzy_search_directory(directory, keyword)

# 打印匹配到的文件路径
# for file_path in found_files:
#     copy_file(file_path, directory1)
#     print(file_path)


# folder_path = 'D:/game/steam/Steam/steamapps/workshop/content/431960'  # 替换为实际的文件夹路径
# print(os.path.exists('E:/night/0730_wallper'))
# printFilesWithTime(getFilesByTime(folder_path, 34))

# printDirs(search("E:/night/0910/0507_view", "x"))

