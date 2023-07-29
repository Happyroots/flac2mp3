import os
import re
folder_path = 'F:\\musics\\随便听听'  # 文件夹路径

# 遍历文件夹中的所有文件,去除文件空格
for filename in os.listdir(folder_path):
    if re.search(r'\xa0', filename):
    # if '\xa0' in filename:
        # 构建原始文件路径和新文件路径
        original_path = os.path.join(folder_path, filename)
        # new_filename = filename.encode('latin1').decode('utf-8').replace('\xa0', '')  # 替换和解码
        # new_filename = filename.replace(' ', '-')  # 去除空格
        new_filename = re.sub(r'\xa0', '-', filename)  # 去除不间断空格
        new_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(original_path, new_path)
        print(f"Renamed {filename} to {new_filename}")

print("File renaming completed.")