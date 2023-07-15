from PIL import Image

def resize_image(input_path, output_path, new_size):
    # 打开图像
    with Image.open(input_path) as image:
        # 调整大小
        resized_image = image.resize(new_size)
        # 保存图像
        print(resized_image)
        resized_image.save(output_path)

# 示例用法
# input_image_path = "./figures/22_EG_CAT.png"
# output_image_path = "figures/22_EG_CAT.png"
new_size = (2500, 1400)

#conding=utf8
import os

g = os.walk(r"./figures/")
for path,dir_list,file_list in g:
    for file_name in file_list:
        print(os.path.join(path, file_name) )
        resize_image(os.path.join(path, file_name), os.path.join(path, file_name), new_size)
