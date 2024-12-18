# `py_platform`

`py_platform` is a script that shows information about your system. It mainly uses the `platform` module in Python.

## Usage

### Running 

You can use `py_platform` by opening it through [Python](https://python.org/). *Latest version of Python used was [`3.11.11`](https://www.python.org/downloads/release/python-31111/)*

### Arguments

#### Freedesktop OS Release info : `-f`, `--freedesktop`

> [!WARNING]
> This argument may crash the script if your computer does not have the `/etc/os-release` file.

This argument shows the output of `platform.freedesktop_os_release()`, which shows JSON-formatted information about your system from `/etc/os-release`.

#### Win32 info : `-w`, `--win32`

This argument shows the output of `platform.win32_ver()`, `platform.win32_edition()`, and `platform.win32_is_iot()`.

- **`platform.win32_ver()`** / **Version**: Shows the version of Windows you are running.

- **`platform.win32_edition()`** / **Edition**: Shows the edition of Windows.

- **`platform.win32_is_iot()`** / **Is IoT / Is Embedded**: Shows whether or not your system is Windows IoT/Embedded (?)

#### macOS info : `-m`, `--mac`

This argument shows the output of `platform.mac_ver()`.

- **`platform.mac_ver()`** / **Version**: Shows the version of macOS you are running.

#### Help : `-h`, `--help`

This argument shows help about how to use the script.
