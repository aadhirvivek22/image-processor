import os.path

def process_folder(folder_path, output_path):
    if not os.path.exists(folder_path) or not os.path.isdir(output_path):
        raise FileNotFoundError(f"The folder {folder_path} does not exist.")
    
    path_list = []
    for file in os.listdir(folder_path):
        if file.lower().endswith((".png",".jpg",".jpeg", ".webp")):
            output_file = file.split('.')[0] + "_compressed" + ".jpg"
            path_list.append((os.path.join(folder_path, file), os.path.join(output_path, output_file)))

    return path_list
