import os
import shutil
import time


files_ext= [".pdf", ".doc", ".docx", ".exe", ".jpg", ".png", ".jfif", ".jpeg", ".zip", ".rar"]
download_dir_path = r'C:\Users\LENOVO\Downloads'
download_pdf_path = r'D:\Downloaded_pdfs'
download_exe_path = r'D:\Downloaded_exe'
download_image_path = r'D:\Downloaded_images'
download_docx_path = r'D:\Downloaded_docx'
download_zip_path = r'D:\Downloaded_rar'


def move(file, source, destination):
    source = source + "\\" + file
    destination = destination +"\\"+ file
    try:
        shutil.move(source, destination)
        print("moved Successfully")
    except:
        print("Failed")

files_list = os.listdir(download_dir_path)

f_list = []
for i in files_list:
    if any(i.endswith(x) for x in files_ext):
        f_list.append(i)
        print(i)

print("Number of pdf files to be moved are ",len(f_list))

for i in range(len(f_list)):
    if any(f_list[i].endswith(x) for x in [".doc", ".docx"]):
        print(f_list[i])
        move(f_list[i], download_dir_path, download_docx_path)
    elif f_list[i].endswith(".exe"):
        print(f_list[i])
        move(f_list[i], download_dir_path, download_exe_path)
    elif f_list[i].endswith(".pdf"):
        print(f_list[i])
        move(f_list[i], download_dir_path, download_pdf_path)
    elif any(f_list[i].endswith(x) for x in [".jpg", ".png", ".jpeg", ".jfif"]):
        print(f_list[i])
        move(f_list[i], download_dir_path, download_image_path)
    elif any(f_list[i].endswith(x) for x in [".rar", ".zip"]):
        print(f_list[i])
        move(f_list[i], download_dir_path, download_zip_path)
    else:
        continue
    

