#!/usr/bin/env python3
import platform, argparse, os, time

# This allows for the user to pass arguments to the script, allowing for certain information to be shown:
parser = argparse.ArgumentParser('py_platform', description='Python-based system information giver using platform module', epilog='thanks! ; main Branch ; updated 2025-01-11 ; by Nacroni')
parser.add_argument('-f', '--freedesktop', help='prints the freedesktop.org OS release information in /etc/os-release', action='store_true')
parser.add_argument('-w', '--win32', help='prints Win32 information', action='store_true')
parser.add_argument('-m', '--mac', help='prints macOS information', action='store_true')
args = parser.parse_args()

# This allows the script to see whether or not a certain argument is enabled.
freedesktop_enable = args.freedesktop
if freedesktop_enable == True and not os.path.exists('/etc/os-release'): # if the argument is true but the file that platform reads doesnt exist
    print('freedesktop argument called yet /etc/os-release doesn\'t exist! Turning off argument...')
    freedesktop_enable = False # turns off argument to prevent crashes that may happen with linux oses without /etc/os-release
win32_enable = args.win32
mac_enable = args.mac

print('System Information')

# I'm sorry about the method I use for variables, but it does the job. =3
system = platform.system()
user = os.getlogin()
hostname = platform.node()
uptime_monotonic = time.monotonic()
release = platform.release()
version = platform.version()
machine = platform.machine()
processor = platform.processor()
processor_count = os.cpu_count()

#    (f'    name:         {var}'             )
print(f'    System:       {system}'          )
print(f'    User:         {user}'            )
print(f'    Hostname:     {hostname}'        )
print(f'    Uptime Awake: {uptime_monotonic}')
print(f'    Release:      {release}'         )
print(f'    Version:      {version}'         )
print(f'    Machine:      {machine}'         )
print(f'    Processor:    {processor}'       )
print(f'    Proc. Amount: {processor_count}' )

if freedesktop_enable: # If the 'freedesktop' argument is used...
    print()
    print('freedesktop.org Information')
    freedesktop_release = platform.freedesktop_os_release()
    print(f'    OS Release: {freedesktop_release}')

if 'Windows' in system or win32_enable: # If the user is running Windows or the Win32 argument is used...
    print()
    print('Windows (Win32) Information')
    win32_ver = platform.win32_ver()
    win32_ed = platform.win32_edition()
    win32_is_iot = platform.win32_is_iot()
    print(f'    Version: {win32_ver}'   )
    print(f'    Edition: {win32_ed}'    )
    print(f'    Is IoT:  {win32_is_iot}')
    
if 'Darwin' in system or mac_enable: # If the user is running Darwin or the Mac argument is used...
    print()
    print('macOS / Darwin Information')
    mac_ver = platform.mac_ver()
    print(f'    Version: {mac_ver}')

print()
print('Python Information')

python_ver = platform.python_version()
python_br = platform.python_branch()
python_build = platform.python_build()
python_comp =  platform.python_compiler()
python_imp = platform.python_implementation()
python_rev = platform.python_revision()

#    (f'    name:           {var}'         )
print(f'    Version:        {python_ver}'  )
print(f'    Branch:         {python_br}'   )
print(f'    Build:          {python_build}')
print(f'    Compiler:       {python_comp}' )
print(f'    Implementation: {python_imp}'  )
print(f'    Revision:       {python_rev}'  )
