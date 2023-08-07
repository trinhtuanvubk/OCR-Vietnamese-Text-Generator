import shutil
import os

def split_data(img_src, label_src, img_des, label_des, ratio=0.9):
  """Moves 10% of the files in a folder to 5 other folders.

  Args:
    folder_path: The path to the folder to move files from.
    destination_folders: A list of paths to the folders to move files to.

  Returns:
    The number of files moved.
  """
  
  print(img_src)
  img_files = os.listdir(img_src)
  label_files = os.listdir(label_src)
  number_of_files = len(img_files)
  print(number_of_files)
  number_of_files_to_move = int((1.0-ratio) * number_of_files)
  print(number_of_files_to_move)
  moved_files = 0

  for img_file in img_files:
      if moved_files < number_of_files_to_move:
          print(os.path.join(img_src, img_file), img_des)
          print(os.path.join(label_src, img_file.split(".")[0] + ".txt"), label_des)
          
          shutil.move(os.path.join(img_src, img_file), img_des)
          shutil.move(os.path.join(label_src, img_file.split(".")[0] + ".txt"), label_des)
          moved_files += 1


  return moved_files

def remove_long_text(img_src, label_src, img_des, label_des):
  """Moves 10% of the files in a folder to 5 other folders.

  Args:
    folder_path: The path to the folder to move files from.
    destination_folders: A list of paths to the folders to move files to.

  Returns:
    The number of files moved.
  """
  
  print(img_src)
  img_files = os.listdir(img_src)
  label_files = os.listdir(label_src)
  val_label_files = os.listdir(label_des)
  # number_of_files = len(img_files)
  # print(number_of_files)
  # number_of_files_to_move = int(0.15 * number_of_files)
  # print(number_of_files_to_move)
  removed_files = 0

  for label_file in label_files:
      # if moved_files < number_of_files_to_move:
    f = open(os.path.join(label_src, label_file), "r")
    text = f.readlines()[0]
    if len(text) > 25:
       
      print(os.path.join(img_src, label_file.split(".")[0] + ".jpg"))
      print(os.path.join(label_src, label_file))
      os.remove(os.path.join(img_src, label_file.split(".")[0] + ".jpg"))
      os.remove(os.path.join(label_src, label_file))
    # os.remove(os.path.join(img_src, img_file), img_des)
    # os.remove(os.path.join(label_src, img_file.split(".")[0] + ".txt"), label_des)
      removed_files += 1
  
  for label_file in val_label_files:
      # if moved_files < number_of_files_to_move:
    f = open(os.path.join(label_des, label_file), "r")
    text = f.readlines()[0]
    if len(text) > 25:
      
      
      print(os.path.join(img_des, label_file.split(".")[0] + ".jpg"))
      print(os.path.join(label_des, label_file))
      os.remove(os.path.join(img_des, label_file.split(".")[0] + ".jpg"))
      os.remove(os.path.join(label_des, label_file))
    # os.remove(os.path.join(img_src, img_file), img_des)
    # os.remove(os.path.join(label_src, img_file.split(".")[0] + ".txt"), label_des)
      removed_files += 1


  return removed_files


if __name__ == "__main__":
  ROOT = "./out/train"
  DES = "./out/val"
  # images = ["images10", "images11", "images12", "images13", "images14", "images15", "images16", "images17" ]
  # labels = ["labels10", "labels11", "labels12", "labels13", "labels14", "labels15", "labels16", "labels17" ]
  #   destination_folders = ["images10", "images11", "images12", "images13", "images14", "images15", "images16", "images17" ]
  number_of_files_moved = 0

  for i in range(1,2):
      # img_src = os.path.join(ROOT, f'images{i}')
      # label_src = os.path.join(ROOT, f'labels{i}')

      # img_des = os.path.join(DES, f'images{i}')
      # os.makedirs(img_des, exist_ok=True)
      # label_des = os.path.join(DES, f'labels{i}')
      # os.makedirs(label_des, exist_ok=True)

      img_src = os.path.join(ROOT, f'images46')
      label_src = os.path.join(ROOT, f'labels46')

      img_des = os.path.join(DES, f'images46')
      os.makedirs(img_des, exist_ok=True)
      label_des = os.path.join(DES, f'labels46')
      os.makedirs(label_des, exist_ok=True)

      number_of_files_moved += split_data(img_src, label_src, img_des, label_des)
      # number_of_files_moved += remove_long_text(img_src, label_src, img_des, label_des)

  print(f"Moved {number_of_files_moved} files.")
