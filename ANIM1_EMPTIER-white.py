import os
from PIL import Image
import shutil


folderIn = r'ANIM1'
folderOn = r'ANIM2'
folderOut = r'OUTPUT'
files = os.listdir(folderIn)
times=0

print("Starting")
def insert_image(main_image_path, save_path):
  main_image = Image.open(main_image_path).convert('RGBA')
  main_width, main_height = main_image.size
    
  for xr in range(main_image.width):
    for yr in range(main_image.height):
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
        OUTPUT = os.path.join(folderOut, search_framepbmp)
        print(f"Doing {times}/1050")
        
        insert_image(ANIM1, OUTPUT)
			
shutil.copy2('ANIM1\liste.txt', 'OUTPUT\liste.txt')
print("Copied liste.txt from anim1 to output folder")
print("DONE")


#####
