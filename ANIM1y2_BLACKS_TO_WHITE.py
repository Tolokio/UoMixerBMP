import os
from PIL import Image
import shutil


folderIn = r'ANIM1'
folderOn = r'ANIM2'
folderOut = r'OUTPUT'
files = os.listdir(folderIn)
files2 = os.listdir(folderOn)
times=0

print("Starting")
def insert_image(main_image_path, save_path):
  main_image = Image.open(main_image_path)
  main_width, main_height = main_image.size
    
  for xr in range(main_image.width):
    for yr in range(main_image.height):
      
      pixel = main_image.getpixel((xr, yr))
      if pixel == (0, 0, 0):
        main_image.putpixel((int(xr), int(yr)), (255, 255, 255))

  # Guarda la imagen de destino
  main_image.save(save_path,"BMP")
  
for file in files:
    times +=1
    if file.endswith(".bmp"):
        search_framepbmp = file
        search_framep= search_framepbmp.replace(".bmp", "")
        search_frame= search_framep.replace("_", ":")
                
        ANIM1 = os.path.join(folderIn, search_framepbmp)
        OUTPUT = os.path.join(folderIn, search_framepbmp)
        print(f"ANIM1-> {times}/1050")
        
        insert_image(ANIM1, OUTPUT)
times = 0
for file in files2:
    times +=1
    if file.endswith(".bmp"):
        search_framepbmp = file
        search_framep= search_framepbmp.replace(".bmp", "")
        search_frame= search_framep.replace("_", ":")
                
        ANIM1 = os.path.join(folderOn, search_framepbmp)
        OUTPUT = os.path.join(folderOn, search_framepbmp)
        print(f"ANIM2-> {times}/1050")
        
        insert_image(ANIM1, OUTPUT)
			
print("FRAMES SAVED ON SAME FOLDER, NOT AT OUTPUT")


#####
