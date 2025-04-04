#!/usr/bin/env python3
import platform, argparse, os, time, logging

# This allows for the user to pass arguments to the script, allowing for certain information to be shown:
parser = argparse.ArgumentParser('py_platform', description='Python-based system information giver using platform module', epilog='thanks! ; main Branch ; by Nacroni')
parser.add_argument('-f', '--freedesktop', help='prints the freedesktop.org OS release information', action='store_true')
parser.add_argument('-a', '--android', help='prints Android information', action='store_true')
parser.add_argument('-w', '--win32', help='prints Win32 information', action='store_true')
parser.add_argument('-d', '--darwin', help='prints Darwin information', action='store_true')
parser.add_argument('-i', '--ios', help='prints iOS information', action='store_true')
parser.add_argument('-o', '--other', help='prints other information', action='store_true')
args = parser.parse_args()

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

# This allows the script to see whether or not a certain argument is enabled.
freedesktop_enable = args.freedesktop
android_enable = args.android
win32_enable = args.win32
darwin_enable = args.darwin
ios_enable = args.ios
other_enable = args.other

print('System Information')

#    (f'    name:         {var}'                    )
print(f'    System:       {platform.system()}'      )
print(f'    User:         {os.getlogin()}'          )
print(f'    Hostname:     {platform.node()}'        )
print(f'    Monotonic:    {time.monotonic()}'       )
print(f'    Release:      {platform.release()}'     )
print(f'    Version:      {platform.version()}'     )
print(f'    Machine:      {platform.machine()}'     )
print(f'    Processor:    {platform.processor()}'   )
print(f'    Architecture: {platform.architecture()}')
print(f'    CPU Count:    {os.cpu_count()}'         )

if freedesktop_enable: # If the 'freedesktop' argument is used...
  print('\nfreedesktop.org Information')
  #    (f'    name:       {var}'                              )
  print(f'    OS Release: {platform.freedesktop_os_release()}')

if android_enable: # If the Android argument is used...
  print('\nAndroid Information')
  #    (f'    name:    {var}'                   )
  print(f'    Version: {platform.android_ver()}')

if 'Windows' in platform.system() or win32_enable: # If the user is running Windows or the Win32 argument is used...
  print('\nWindows (Win32) Information')
  #    (f'    name:    {var}'                     )
  print(f'    Version: {platform.win32_ver()}'    )
  print(f'    Edition: {platform.win32_edition()}')
  print(f'    Is IoT:  {platform.win32_is_iot()}' )
    
if 'Darwin' in platform.system() or darwin_enable: # If the user is running Darwin or the Mac argument is used...
  print('\nDarwin Information')
  #    (f'    name:        {var}'               )
  print(f'    Mac Version: {platform.mac_ver()}')

if ios_enable: # If the iOS argument is used...
  print('\niOS Information')
  #    (f'    name:        {var}'               )
  print(f'    iOS Version: {platform.ios_ver()}')

print('\nPython Information')

#    (f'    name:           {var}'                             )
print(f'    Version:        {platform.python_version()}'       )
print(f'    Branch:         {platform.python_branch()}'        )
print(f'    Build:          {platform.python_build()}'         )
print(f'    Compiler:       {platform.python_compiler()}'      )
print(f'    Implementation: {platform.python_implementation()}')
print(f'    Revision:       {platform.python_revision()}'      )

if other_enable:
  print('\nOther Information')
  #    (f'    name:         {var}'                )
  print(f'    libc Version: {platform.libc_ver()}')
