#!/usr/bin/env python3
import platform, argparse, os, time

# This allows for the user to pass arguments to the script, allowing for certain information to be shown:
parser = argparse.ArgumentParser('py_platform', description='Python-based system information giver using platform module', epilog='thanks! ; main Branch ; updated 2025-01-27 ; by Nacroni')
parser.add_argument('-f', '--freedesktop', help='prints the freedesktop.org OS release information in /etc/os-release', action='store_true')
parser.add_argument('-w', '--win32', help='prints Win32 information', action='store_true')
parser.add_argument('-m', '--mac', help='prints macOS information', action='store_true')
args = parser.parse_args()

# This allows the script to see whether or not a certain argument is enabled.
freedesktop_enable = args.freedesktop
if freedesktop_enable == True and not os.path.exists('/etc/os-release'): # if the argument is true but the file that platform reads doesnt exist
    print('freedesktop argument called yet /etc/os-release doesn\'t exist! Turning off argument...')
    freedesktop_enable = False # turns off argument to prevent crashes that may happen with linux-identifying oses without /etc/os-release
win32_enable = args.win32
mac_enable = args.mac

print('System Information')

#    (f'    name:             {var}'                 )
print(f'    System:           {platform.system()}'   )
print(f'    User:             {os.getlogin()}'       )
print(f'    Hostname:         {platform.node()}'     )
print(f'    Uptime Monotonic: {time.monotonic()}'    )
print(f'    Release:          {platform.release()}'  )
print(f'    Version:          {platform.version()}'  )
print(f'    Machine:          {platform.machine()}'  )
print(f'    Processor:        {platform.processor()}')
print(f'    CPU Count:        {os.cpu_count()}'      )

if freedesktop_enable: # If the 'freedesktop' argument is used...
    print()
    print('freedesktop.org Information')
    #    (f'    name:       {var}'                              )
    print(f'    OS Release: {platform.freedesktop_os_release()}')

if 'Windows' in platform.system() or win32_enable: # If the user is running Windows or the Win32 argument is used...
    print()
    print('Windows (Win32) Information')
    #    (f'    name:    {var}'                     )
    print(f'    Version: {platform.win32_ver()}'    )
    print(f'    Edition: {platform.win32_edition()}')
    print(f'    Is IoT:  {platform.win32_is_iot()}' )
    
if 'Darwin' in platform.system() or mac_enable: # If the user is running Darwin or the Mac argument is used...
    print()
    print('Darwin Information')
    mac_ver = platform.mac_ver()
    #    (f'    name:    {var}'    )
    print(f'    Version: {mac_ver}')

print()
print('Python Information')

#    (f'    name:           {var}'                             )
print(f'    Version:        {platform.python_version()}'       )
print(f'    Branch:         {platform.python_branch()}'        )
print(f'    Build:          {platform.python_build()}'         )
print(f'    Compiler:       {platform.python_compiler()}'      )
print(f'    Implementation: {platform.python_implementation()}')
print(f'    Revision:       {platform.python_revision()}'      )
