import os
from PIL import Image
import shutil


folderIn = r'ANIM1'
folderOn = r'ANIM2'
folderOut = r'OUTPUT'
files = os.listdir(folderIn)
times=0

print("Starting")
def insert_image(main_image_path, insert_image_path, save_path, centerx, centery):
  main_image = Image.open(main_image_path)
  insert_image = Image.open(insert_image_path)
  main_width, main_height = main_image.size
  insert_width, insert_height = insert_image.size
  x = centerx
  y = centery
  y = int(main_height) + y - insert_height
    
  for xr in range(main_image.width):
    for yr in range(main_image.height):
      xx= xr-x
      yy= yr-y
      if (0 <= xx <= int(insert_image.width - 1)) and (0 <= yy <= int(insert_image.height - 1)):
        pixel = insert_image.getpixel((xx, yy))
        if (pixel == (0, 0, 0)) or (pixel == (255, 255, 255)):
          main_image.putpixel((int(xr), int(yr)), (255, 255, 255))
      else:
        main_image.putpixel((int(xr), int(yr)), (255, 255, 255))

  # Guarda la imagen de destino
  main_image.save(save_path)

warnings_1=0  
for file in files:
    times +=1
    if file.endswith(".bmp"):
        search_framepbmp = file
        search_framep= search_framepbmp.replace(".bmp", "")
        search_frame= search_framep.replace("_", ":")
        WEREABLE = os.path.join(folderOn, search_framepbmp)
        if os.path.exists(WEREABLE)==False:
          print("++++++++++++++++++++++++++++WARNING!!")
          print(WEREABLE)
          print("NOT FOUND")
          warnings_1 +=1
          continue
        with open(r'ANIM1\liste.txt', 'r') as posiciones1:
            for i, line in enumerate(posiciones1):
                if search_frame in line:
                    n_linea=i + 1
                if n_linea == i:
                    CenterX=line.strip()
                    Xt=CenterX.replace("CenterX:", "")
                elif n_linea == i - 1:
                    CenterY=line.strip()
                    Yt=CenterY.replace("CenterY:", "")
                    n_linea=""
                    break
        with open(r'ANIM2\liste.txt', 'r') as posiciones2:
            for ii, line in enumerate(posiciones2):
                if search_frame in line:
                    n_linea=ii + 1
                if n_linea == ii:
                    CenterX=line.strip()
                    Xw=CenterX.replace("CenterX:", "")
                if n_linea == ii - 1:
                    CenterY=line.strip()
                    Yw=CenterY.replace("CenterY:", "")
                    n_linea=""
                    break

        X= int(Xt) - int(Xw)
        Y= -int(Yw) + int(Yt)
                 
        TEMPLATE = os.path.join(folderIn, search_framepbmp)
        OUTPUT = os.path.join(folderOut, search_framepbmp)
        print(f"Doing {times}/1050")
        
        insert_image(TEMPLATE, WEREABLE, OUTPUT, X, Y)
			
shutil.copy2('ANIM1\liste.txt', 'OUTPUT\liste.txt')
print("")
print("DONE")
print("")
if warnings_1 > 0:
  print("WARNINGS missing frames at anim1 folder:")
  print(warnings_1)
#####
