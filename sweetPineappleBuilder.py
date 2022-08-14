# -*- coding: utf-8 -*-

# Author:   Naqwada (Necrum Security Labs - NSLabs) <naqwada@pm.me>
# License:  MIT License (http://www.opensource.org/licenses/mit-license.php)
# Docs:     https://github.com/Naqwa/Sweet-Pineapple-Builder
# Website:  http://samy.link/
# Linkedin: https://www.linkedin.com/in/samy-younsi/
# Note:     FOR EDUCATIONAL PURPOSE ONLY.

from __future__ import print_function, unicode_literals
from PyInquirer import Separator, Token, prompt, style_from_dict
from termcolor import cprint
import subprocess
import random
import time
import os

def banner():
  pineappleLogo = """
                                ▒▒██░░                        ░░██▒▒                                  
██╗    ██╗██╗███████╗██╗        ██▓▓██                        ██▓▓██                                                                
██║    ██║██║██╔════╝██║        ▓▓▓▓██                        ██▓▓██                                  
██║ █╗ ██║██║█████╗  ██║  ▒▒████▒▒████████▓▓█████▓▓███████████▓▓██▓▓██████                            
██║███╗██║██║██╔══╝  ██║  ▓▓▒▒▒▒▒▒+++▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒SWEET▒PINEAPPLE▒▒██                                                     
╚███╔███╔╝██║██║     ██║  ██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒BUILDER▒▒▒V1.02▒▒██                                                     
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                                      
                               ██▓▓▓▓██                      ██▓▓▓▓██                                           
██████╗ ██╗███╗   ██╗███████╗ █████╗ ██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║████╗  ██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██╔██╗ ██║█████╗  ███████║██████╔╝██████╔╝██║     █████╗  
██╔═══╝ ██║██║╚██╗██║██╔══╝  ██╔══██║██╔═══╝ ██╔═══╝ ██║     ██╔══╝  
██║     ██║██║ ╚████║███████╗██║  ██║██║     ██║     ███████╗███████╗
╚═╝     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚══════╝
                                                                 
██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗        \||/ 
██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗       \||/
██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝     .<><><>.
██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗    .<><><><>.
██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║    '<><><><>'
╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝     '<><><>'
Author: Naqwada (Samy Younsi)                             v1.0.2
Necrum Security Labs (NSLabs)
  """
  txtColors = ['red', 'green', 'cyan', 'yellow', 'blue', 'magenta']
  return cprint(pineappleLogo, random.choice(txtColors), attrs=['bold'])


def checkDependencies():
    try:
        cprint('[+] Installing dependencies ...', 'blue', attrs=['bold'])
        cprint('[+] sudo apt-get install binwalk awk build-essential -y', 'blue', attrs=['bold'])
        subprocess.run('sudo apt-get install build-essential binwalk gawk -y', shell=True)
        cprint('[+] Dependencies has been successfully installed on this machine!', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def downloadPineappleFw():
    try:
        cprint('[+] Downloading the latest version of WiFi Pineapple Tetra ...', 'blue', attrs=['bold'])
        pineappleFwUrl = 'https://www.wifipineapple.com/downloads/tetra/latest'
        subprocess.run('wget {} -O cake/tetrafw.bin'.format(pineappleFwUrl), shell=True)
        cprint('[+] WiFi Pineapple Tetra firmware has been successfully downloaded!', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])
 

def unpackPineappleFw():
    try:
        cprint('[+] Unpacking WiFi Pineapple Tetra Firmware...', 'blue', attrs=['bold'])
        subprocess.run('binwalk -eM cake/tetrafw.bin', shell=True)
        cprint('[+] WiFi Pineapple Tetra firmware has been successfully unpacked!', 'green', attrs=['bold'])    
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {}, and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def extractPineappleOverlay():
    try:
        cprint('[+] Extraction of the Pineapple Tetra WiFi overlay from the OpenWrt firmware...', 'blue', attrs=['bold'])
        overlayFile = open('cake/seed/overlay.txt', 'r')
        for filePath in overlayFile:
            directory = os.path.dirname(filePath)
            fileName = os.path.basename(filePath)
            fullpath = 'cake/_tetrafw.bin.extracted/sysupgrade-pineapple-tetra/_root.extracted/squashfs-root{}'.format(directory)
            if os.path.isdir(fullpath):
                subprocess.run('mkdir -p cake/overlay{}'.format(directory.strip()), shell=True)
            subprocess.run('cp -r {}/{} ./cake/overlay{}'.format(fullpath.strip(), fileName.strip(), directory.strip()), shell=True)
        cprint('[+] Overlay succefully extracted...', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def updatedRootPassword():
    try:
        cprint('[+] Updating shadow file and replace default Pineapple password for root user.', 'blue', attrs=['bold'])
        shadowFile = 'cake/overlay/etc/shadow'
        passwordHash = '$1$YxFLPZho$24cgp7UqDzHVvzJWWJqvm1' # root
        user = open(shadowFile,'r')
        userData = user.read()
        user.close()
        newUserData = userData.replace('$1$DhqYuxhs$p/O7aro1npF4yvkRT7qJK.', passwordHash)
        user = open(shadowFile,'w')
        user.write(newUserData)
        user.close()
        cprint('[+] Shadow file has been updated. New password: root/root', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def replaceExtFileSystemScript():
    try:
        cprint('[+] Replacing the script 20-sd with a custom one to spend the router storage space with a USB stick.', 'blue', attrs=['bold'])
        subprocess.run('cp cake/seed/custom-20-sd.sh cake/overlay/etc/hotplug.d/block/20-sd', shell=True)
        cprint('[+] Script 20-sd has been replaced.', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def downloadOpenwrtImageBuilder():
    try:
        cprint('[+] Downloding OpenWrt Image Builder (ar71xx-generic).', 'blue', attrs=['bold'])
        imageBuilderUrl = 'https://archive.openwrt.org/releases/19.07.2/targets/ar71xx/generic/openwrt-imagebuilder-19.07.2-ar71xx-generic.Linux-x86_64.tar.xz'
        subprocess.run('wget {} -O cake/openwrt-imagebuilder.tar.xz'.format(imageBuilderUrl), shell=True)
        cprint('[+] Openwrt Image Builder (ar71xx-generic) has been successfully downloaded!', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def extractOpenwrtImageBuilder():
    try:
        cprint('[+] Extracting OpenWrt Image Builder...', 'blue', attrs=['bold'])
        subprocess.run('tar -xf cake/openwrt-imagebuilder.tar.xz -C cake', shell=True)
        cprint('[+] OpenWrt Image Builder successfully extracted.', 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def buildCustomPineappleImage(routerName):
    try:
        cprint('[+] Building custom WiFi Pineapple Tetra firmware for the {} router.'.format(routerName), 'blue', attrs=['bold'])
        #Fixed a small bug with requirement checking because GCC version 11 does not exist two years ago.
        subprocess.run('cp cake/seed/prereq-build.mk cake/openwrt-imagebuilder-19.07.2-ar71xx-generic.Linux-x86_64/include/prereq-build.mk', shell=True)
        opkgFile = open('cake/seed/opkg.txt', 'r')
        opkgList = opkgFile.read()
        opkgFile.close()
        cmd = 'sudo make -C cake/openwrt-imagebuilder-19.07.2-ar71xx-generic.Linux-x86_64/ image PROFILE={} PACKAGES="{}" FILES=cake/overlay/'.format(routerName, opkgList)
        subprocess.run(cmd, shell=True)
        cprint('[🎉] Congratulation! Your Pineapple Tetra WiFi firmware for the router {} has been successfully compiled.'.format(routerName), 'green', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def cleaning(routerName):
    try:
        cprint('[+] Cleaning...', 'blue', attrs=['bold'])
        subprocess.run('mkdir -p cake/customFW && cp cake/openwrt-imagebuilder-19.07.2-ar71xx-generic.Linux-x86_64/bin/targets/ar71xx/generic/*.bin cake/customFW && sudo rm -rf cake/openwrt-imagebuilder.tar.xz cake/tetrafw.bin cake/_tetrafw.bin.extracted cake/openwrt-imagebuilder-19.07.2-ar71xx-generic.Linux-x86_64 cake/overlay/*', shell=True)

        cprint('\n\n[INFO] The custom firmware can be found under cake/customFW/.'.format(routerName), 'cyan', attrs=['bold'])
        cprint('[INFO] The next step is to install the firmware in your device.\n[NOTE] If you are having difficulties, please consult my blog post about the this project (https://samy.link/blog/build-your-own-wifi-pineapple-tetra-for-7). You will find the next steps to follow.'.format(routerName), 'cyan', attrs=['bold'])
    except Exception as e:
        cprint('[ERROR] An error occurs... copy this error: {} and create an issue on GitHub.'.format(e), 'green', attrs=['bold'])


def main():
  banner()
  print('[🍍] Hi there, let\'s cook a nice and tasty pineapple cake!\n')
  time.sleep(2)
  try:
      answer = prompt(selectRouter, style=promptStyle)
      cprint('[✔️] Router {} selected'.format(answer['router']), 'green', attrs=['bold'])
      
      binwalkPath = checkDependencies()
      downloadPineappleFw()
      unpackPineappleFw()
      extractPineappleOverlay()
      updatedRootPassword()
      replaceExtFileSystemScript()
      downloadOpenwrtImageBuilder()
      extractOpenwrtImageBuilder()
      buildCustomPineappleImage(answer['router'])
      cleaning(answer['router'])
  except Exception as e:
    print('\n[👹] See you soon for a new adventure!\n')


selectRouter = [
    {
        'type': 'list',
        'name': 'router',
        'qmark': '[❓]',
        'message': 'Select the router you wish to convert in WiFi Pineapple Tetra.',
        'choices': [ 
            Separator('--- Buffalo ---'),
            {
                'name': 'WZR450HP2',
            },
            {
                'name': 'WZR600DHP',
            },
            {
                'name': 'WZRHPAG300H'
            },
            {
                'name': 'WZRHPG300NH'
            },
            {
                'name': 'WZRHPG300NH2'
            },
            {
                'name': 'WZRHPG450H\n'
            },
            Separator('--- D-Link ---'),
            {
                'name': 'DGL5500A1'
            },
            {
                'name': 'DIR835A1',
            },
            {
                'name': 'dir-869-a1\n'
            },
            Separator('--- GL.iNet ---'),
            {
                'name': 'gl-ar300'
            },
            {
                'name': 'gl-ar300m',
            },
            {
                'name': 'gl-ar750',
            },
            {
                'name': 'gl-ar750s\n'
            },
            Separator('--- TP-Link ---'),
            {
                'name': 'archer-c7-v2'
            },
            {
                'name': 'archer-c7-v4'
            },
            {
                'name': 'archer-c7-v5'
            },
            {
                'name': 'archer-c60-v1'
            },
            {
                'name': 'archer-c60-v2\n'
            },
        ]
    }
]

promptStyle = style_from_dict({
    Token.Separator: '#b41e44 bold',
    Token.QuestionMark: '#4b7bec',
    Token.Selected: '#b41e44 bold',
    Token.Pointer: '#45aaf2 bold',
    Token.Instruction: '', 
    Token.Answer: '#fff bold',
    Token.Question: '#3498db bold',
})

if __name__ == "__main__":
  main()