import os
from pathlib import Path
import time

pico8 = ""
tic80 = ""
cmdpico8 = ""
cmdtic80 = ""

path = Path("./bootloaderdata.txt")

#First run check/setup
os.system('cls' if os.name == 'nt' else 'clear')
if os.path.exists(path) == False:
    print("""
        dMMMMMP .aMMMb  dMMMMb dMMMMMMP .aMMMb  .dMMMb  dMP dMP         dMMMMb  .aMMMb  .aMMMb dMMMMMMP dMP    .aMMMb  .aMMMb  dMMMMb  dMMMMMP dMMMMb 
       dMP     dMP"dMP dMP dMP   dMP   dMP"dMP dMP" VP dMP.dMP         dMP"dMP dMP"dMP dMP"dMP   dMP   dMP    dMP"dMP dMP"dMP dMP VMP dMP     dMP.dMP 
      dMMMP   dMMMMMP dMP dMP   dMP   dMMMMMP  VMMMb   VMMMMP         dMMMMK" dMP dMP dMP dMP   dMP   dMP    dMP dMP dMMMMMP dMP dMP dMMMP   dMMMMK"  
     dMP     dMP dMP dMP dMP   dMP   dMP dMP dP .dMP dA .dMP         dMP.aMF dMP.aMP dMP.aMP   dMP   dMP    dMP.aMP dMP dMP dMP.aMP dMP     dMP"AMF   
    dMP     dMP dMP dMP dMP   dMP   dMP dMP  VMMMP"  VMMMP"         dMMMMP"  VMMMP"  VMMMP"   dMP   dMMMMMP VMMMP" dMP dMP dMMMMP" dMMMMMP dMP dMP    
                                                                                                                                                      
    \n
    """)
    print("IMPORTANT: Make sure this script is inside a empty folder.")
    print("Welcome! Since this is your first time lets get you setup. \n")
    welcome = input("Press enter to continue: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Do you have Pico-8? if yes type the command to run the executable if not type no.")
    cmdpico8 = input("Input your path or selection: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Do you have TIC-80? if yes type the command to run the executable if not type no.")
    cmdtic80 = input("Input your path or selection: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    
    #Saving Data
    contents = f"{cmdpico8} \n"
    contents += f"{cmdtic80} \n"
    path.write_text(contents)
else:
    #Loading Data
    contents = path.read_text()
    for line in contents.splitlines():
        cmdpico8 = line[:0]
        cmdtic80 = line[:1]
#Actual program
print("""
    dMMMMMP .aMMMb  dMMMMb dMMMMMMP .aMMMb  .dMMMb  dMP dMP         dMMMMb  .aMMMb  .aMMMb dMMMMMMP dMP    .aMMMb  .aMMMb  dMMMMb  dMMMMMP dMMMMb 
   dMP     dMP"dMP dMP dMP   dMP   dMP"dMP dMP" VP dMP.dMP         dMP"dMP dMP"dMP dMP"dMP   dMP   dMP    dMP"dMP dMP"dMP dMP VMP dMP     dMP.dMP 
  dMMMP   dMMMMMP dMP dMP   dMP   dMMMMMP  VMMMb   VMMMMP         dMMMMK" dMP dMP dMP dMP   dMP   dMP    dMP dMP dMMMMMP dMP dMP dMMMP   dMMMMK"  
 dMP     dMP dMP dMP dMP   dMP   dMP dMP dP .dMP dA .dMP         dMP.aMF dMP.aMP dMP.aMP   dMP   dMP    dMP.aMP dMP dMP dMP.aMP dMP     dMP"AMF   
dMP     dMP dMP dMP dMP   dMP   dMP dMP  VMMMP"  VMMMP"         dMMMMP"  VMMMP"  VMMMP"   dMP   dMMMMMP VMMMP" dMP dMP dMMMMP" dMMMMMP dMP dMP    
                                                                                                                                                  
\n
""")

print("Welcome to Fantasy Bootloader v1.0!")
if cmdpico8.lower() == "" or cmdpico8.lower() == "n" or cmdpico8.lower() == "no":
    pico8 = False
else:
    print("Type Pico to load Pico-8")
if cmdtic80.lower() == "" or cmdtic80.lower() == "n" or cmdtic80.lower() == "no":
    tic80 = False
else:
    print("Type TIC to load TIC-80")
print("Type Quit to Quit")
print("Type Reset to reset to first run to change settings \n")
while True:
    selection = input("Input your selection: ")
    if selection.lower() == "pico":
        if pico8 == False:
            error = input("Pico-8 has not been set up! Press enter to continue:")
            continue
        else:
            os.system(cmdpico8)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
    elif selection.lower() == "tic":
        if pico8 == False:
            error = input("Pico-8 has not been set up! Press enter to continue:")
            continue
        else:
            os.system(cmdtic80)
            os.system('cls' if os.name == 'nt' else 'clear')
            exit()
    elif selection.lower() == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    elif selection.lower() == "reset":
        os.remove(path)
        reset = input("Please press enter to quit and then run the script again to fully reset: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    else:
        error = input("Please type a valid command! Press enter to continue:")
        continue
