import os
import subprocess

# FFmpeg可执行文件路径
ffmpeg_path = 'F:\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'

# 输入.flac文件夹路径
input_folder = 'F:\\musics\\随便听听'

# 输出.mp3文件夹路径
output_folder = 'F:\musics\随便听听\\downloads'



# 遍历输入文件夹中的所有.flac文件
for filename in os.listdir(input_folder):
    if filename.endswith('.flac') or filename.endswith('.m4a') :
        # 构建输入文件和输出文件的完整路径
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + '.mp3')

        # 使用FFmpeg进行转换
        command = f'"{ffmpeg_path}" -i "{input_file}" -c:a libmp3lame -q:a 2 "{output_file}"'
        # command = f'"{ffmpeg_path}" -i "{input_file}" "{output_file}"'

        try:
            subprocess.run(command, check=True)
            print("转换成功！")
        except subprocess.CalledProcessError as e:
            print("转换失败:", e)
        # os.system(command)

        # print(f"Converted {input_file} to {output_file}")

print("Conversion completed.")
