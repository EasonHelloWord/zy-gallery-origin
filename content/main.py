import os
from datetime import datetime, timedelta

# 设置起始日期
start_date = datetime.strptime("2024-03-30", "%Y-%m-%d")

# 获取文件夹列表
folders = [f for f in os.listdir() if os.path.isdir(f) and f.startswith('pic')]

# 排序文件夹
folders.sort(key=lambda x: int(x[3:]))

# 遍历每个文件夹
for i, folder in enumerate(folders):
    # 计算当前日期
    current_date = start_date - timedelta(days=i)
    date_str = current_date.strftime("%Y-%m-%d")
    
    # 新文件夹名称
    new_folder_name = date_str
    
    # 重命名文件夹
    os.rename(folder, new_folder_name)
    
    # 修改index.md文件
    index_md_path = os.path.join(new_folder_name, "index.md")
    if os.path.exists(index_md_path):
        with open(index_md_path, 'r') as file:
            lines = file.readlines()
        
        # 在第二行插入日期
        lines.insert(1, f"date: {date_str}\n")
        
        with open(index_md_path, 'w') as file:
            file.writelines(lines)

    print(f"{folder} renamed to {new_folder_name} and date added to index.md")
