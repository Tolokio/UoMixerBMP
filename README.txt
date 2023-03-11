
//////////////////////////////////////////////////////////////////////////////////////////////////////
This is a set of tool created to make less painful to work with Ultima Online Anims.
Thx to Prapilk, Asylum, Punt and Chatgpt for the assist.

It is very recommended to work using User_Interface.py or idle as u will be able to check logs.
First of all is to create folders. So dclick on create folders file or by the user_interface.py

The rest of the tools are very intuitive, just fill proper folders with proper anims and use the proper tool.
IT is recommended to experiment things just to see what happens.Fill anim1 and anim2 with frames+liste.txt and try all options.

This version works with .BMP files.

[FOLDERS]
-ANIM1->Put here .bmp files + liste.txt (will remain untouch but when u use BlackToWhite or WhitesToBlack.py)
-ANIM2->Put here .bmp files + liste.txt (will remain untouch but when u use BlackToWhite or WhitesToBlack.py)
-OUTPUT->New frames.bmp + liste.txt will be saved here. (will overwritte if OUTPUT is already filled)

[Tools]
Each .py file does what names says it going to do.
For it, u need to put frames+list.txt into specific folder.
Then u can dclick on each .py, use the "user_interface.py" or use idle

ANIM1+ANIM2.py Paste anim2 into anim1
ANIM1-ANIM2.py Remove ANIM2 from ANIM1
ANIM1-A2Contorn.py Remove ANIM2 background pixels from anim1. 
Create_Folders.py Check if folders are created and create them if not. Use it if u rename Output or any folder.(renaming is faster than copying files from folder to another)
Anim1&2_BlacksToWhite.py-> Change background color from black to white. IT will work on .bmp frames present in anim1 and anim2. IT replace the old frames in same folder.
Anim1&2_WhitesToBlack.py-> Change background color from white to black. IT will work on .bmp frames present in anim1 and anim2.  IT replace the old frames in same folder.

[NOTES]
-Number of files at anim1 and anim2 can have diferent, but only frames presents at both Folders will be modified when u mix both folders.
 

[Known Issue]
Some missing frames are ignored and there is no warning for them. There will be warnings only at cases where code would give error and stop working. 
Check the amount of frames of the anims u are going to mix. I haven't decide how to deal with this yet. So in this cases u need to move missing frames manually until I decide the fix.

[FAQ]

Q-How to install python and pil library?
A-Google it or ask chatgpt.

Q-IT is possible to use it with npcs frames?
A-Never tried but should be possible if use similar frames numbers per action and similar actions. Only frames present on both anims will be modified.



