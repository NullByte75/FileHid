import os
import py7zr
import time
import colorama

colorama.init()

print(colorama.Fore.LIGHTBLACK_EX)

banner = """ `+.        -ss-      ::            
                                                          --    .oh:      .+yh+`    `/o-            
                                                         -y+`  -sdd:    .+yhhs.    -sy/      `      
                                                        -ym/ `/hmdy.  .+yhhhs.  `-ohh+`   `-+.      
                                                       :hmh-.sdddh/`.+hdhhh+` `-oyhy/` `./os-       
                                                      /dmd+/hdddh+:oydhhho-``/shdho.`-/oyy+.``..`   
                                                `   `+mNmysddddhoshdddds:.-ohddho::+yhhyo::/o+:`    
                                               -o` .sNNmdhhhhhyyhdddds+/ohmmdhysyhdddysoosso:`      
                                              `yh-:hNNmmdhhyyyhddmmNhhdmmmmmddmmmddhhyys+:.`        
                                             `sNdymNNmNdhyyyyhdmNNNNNmmmmNNmmmmdhhhyyo+////:.       
                                            `sNNNNNNNmddhhhdmmNNNmdmNNNmmmmmmmmdhhhhhhhyo/-`        
                                           .yNNNNmNNNmmmmmNNNNmmmmmmmdmdmmmmmdhhhhhhdhs:`           
                                         `:hNNmmmNNNmmmmmNmmmmdddmmmmmmmmmdhhhhhhhhhy+.`            
                                      ``:ymNmmNNNmmddhdmmmmNmmmmNNNNNmmddhhhhhdddddy:`              
                                     .+hNNNmmddhhhhhdmNNNNNNNNNNNNNNmmmdhyyhhhhhyo:`                
                                    .yNMNmhyssyhdddddddddddddddmmmmmmddyssyhdmmdo.                  
                                    +NNNdhhddmNNmmhhhhhhddddhdddmmddmdhyhhhhdho.`                   
                                   .hMMNdhyyhmddddhyyyhhhdddmmmmmNNNNNmdyo/:/:`                     
                          ````-/+o+smNmmdddhyyyyyssyyyssyhdddmmddmmmmhyyy/`                         
                      -+:ohmhhdmmmmmmdhyyyyyhyhdmddhhhhyyyyhddmmdddmmyyo:`                          
                    `+hdddddmdmmmmmdhys++osyhhdmmmmmdddmmmddhyyyhddhs+-`                            
                   .ohdmmmmmNNNNmdhhyoosyyysshdmmNNmmddmmmmmmdddhs/``                               
                   /hyhdmNNNNNNmddhhyo++osyhddhyyyyhdmdmNmmmmdhs+:.`                                
                  .ydmmmNNNNNNNNmdddhhhyhhddddmmddhhhmmmmmmmmmmhs+.                                 
                 `+hdmmNNmmmNNNNNNNNmddddmNmmmmmmNNNNNmmdddddmmy:.`                                 
                `/hhhyo/:.../o+sdNNNNNNNmmddmmNNNmNNmdddhyys-:oy/                                   
                `shy/`       ``-+shmmmdddmmmmmmNNmmNMho++:::`  `                                    
                `+o-            `.-odmddhddmmmNNNNNNNNdo-`                                          
                 ``                .+dNmhhhdddddmNNNNNNmhs:`                                        
                                    `./hmdddhmdddmmNNNmhhhyo:`                                      
                                       :NmdmmhNmmmmmmmNmdhyyso-`                                    
                                       -NmmmNmdNNNmdhddmddhyyhhs/.`                                 
                                       `sddddmmmNNmy-.:/::::+ydmmyo/.                               
                                        `odddmmmso+.    ``` `-oyhdyss+:.`                           
                                      ``./yddmdh.             `://ooosyyso+/:`                      
                                ```-/oossydmdy++`               ..`..:oyhdddhs:                     
                              `-osssys+s+smd+-..                 ``    `-/ss/-`                     
                              .///..-.-syo:-`                             ``                        
                                  `./os++-                                                          
                                 .+o+oy-.`                                                          
                                .sh+. +s-                                                           
                                .ss-` -/`                                                           
                                `-- 
                                
                                    FILE HIDER 1.0        
                                
                                """
                    

print(banner)

def copyFiles(file, img, newimg):
    os.system("copy /b " + img + '+' + file + ' ' + newimg)

def createArchives(zipname, img, file, passwd):
    cwd = os.getcwd()
    with py7zr.SevenZipFile(zipname, 'w', password=passwd) as archive:
        archive.writeall(cwd,'base')

def unzipArchives(zipname, passwd):
    with py7zr.SevenZipFile(zipname, mode='r', password=passwd) as z:
        z.extractall()

def hide():
    print(colorama.Fore.YELLOW)
    zipname = input(str('Enter archive name (only .7z files): '))
    path_img = input(str('Enter target image: ')) 
    path_file = input(str('Enter target file: '))
    passwd = input(str('Enter password for hidden file: '))
    path_newimg = input(str('Enter new image name (with extension): '))
    print(colorama.Fore.LIGHTBLUE_EX)
    print("Creating archive...")
    createArchives(zipname, path_img, path_file, passwd)
    print('Copying archive into image...')
    copyFiles(zipname, path_img, path_newimg)
    print(colorama.Fore.LIGHTGREEN_EX)
    print('Done!')

def main():
    print(colorama.Fore.LIGHTWHITE_EX)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    print(".", end='')
    time.sleep(1)
    hide()
main()
