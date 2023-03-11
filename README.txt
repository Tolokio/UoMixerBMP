//////////////////////////////
UOMIXER BMP VERSION////////////
///////////////////////

Thx to Prapilk, Asylum, Punt and Chatgpt for the assist.

It is very recommended to work using User_Interface.py or idle as u will be able to check logs.
First of all is to create folders Then fill the folders and use any tool.
IT is recommended to experiment things just to see what happens.Fill anim1 and anim2 with frames.bmp+liste.txt and try all options.

This version works with ONLY with.BMP files and is designed to work with frames extracted with mulpatcher.exe.

[FOLDERS]
-ANIM1->Put here .bmp files + liste.txt (will remain untouch but when u use BlackToWhite or WhitesToBlack.py)
-ANIM2->Put here .bmp files + liste.txt (will remain untouch but when u use BlackToWhite or WhitesToBlack.py)
-OUTPUT->New frames.bmp + liste.txt will be saved here. (will overwritte if OUTPUT is already filled)

[Tools]

ANIM1+ANIM2.py-> Paste anim2 into anim1
ANIM1-ANIM2.py-> Remove ANIM2 from ANIM1
ANIM1-A2Contorn.py-> Remove ANIM2 background pixels from anim1. 
Create_Folders.py-> Check if folders are created and create them if not. Use it if u rename Output or any folder.(renaming is faster than copying files from folder to another)
Anim1&2_BlacksToWhite.py-> Change background color from black to white. IT will work on .bmp frames present in anim1 and anim2. IT replace the old frames in same folder.
Anim1&2_WhitesToBlack.py-> Change background color from white to black. IT will work on .bmp frames present in anim1 and anim2.  IT replace the old frames in same folder.

[NOTES]
-Number of files at anim1 and anim2 can have diferent, but only frames presents at both Folders will be modified when u mix both folders.
 

[Known Issue]
-Some missing frames are ignored and there is no warning for them. There will be warnings only at cases where code would give error and stop working. 
Check the amount of frames of the anims u are going to mix and be aware if are not the same.

[FAQ]

Q-How to install python and pil library?
A-Google it or ask chatgpt.

Q-IT is possible to use it with npcs frames?
A-Never tried but should be possible if use similar frames numbers per action and similar actions. Only frames present on both anims will be modified.



