# `py_platform`

`py_platform` is a script that shows information about your system. It mainly uses the `platform` module in Python.

## Modules Used

> [!NOTE]
> All of these are packed in with Python by default, meaning that there is no need for installing other modules.

- `platform`
- `argparse` *Python 3.2 and above*
- `os`
- `time`

## Usage

### Running

You can use `py_platform` by opening it through [Python](https://python.org/). *Latest version of Python used was [`3.13.2`](https://www.python.org/downloads/release/python-3132/), oldest version of Python used was [`3.11.11`](https://www.python.org/downloads/release/python-31111/) **(This doesn't mean older versions of Python can't be used!)***

### Arguments

#### All info : `-a`, `--all`

This argument shows all of the arguments shown below.

#### Freedesktop OS Release info : `-f`, `--freedesktop`

This argument shows the output of `platform.freedesktop_os_release()`, which shows JSON-formatted information about your system.

#### Android info : `-n`, `--android`

> [!IMPORTANT]
> Not every Python version supports this argument.

This argument shows the output of `platform.android_ver()`.

- **`platform.android_ver()`** / **Version**: Shows the version of Android you are running.

#### Win32 info : `-w`, `--win32`

This argument shows the output of `platform.win32_ver()`, `platform.win32_edition()`, and `platform.win32_is_iot()`.

- **`platform.win32_ver()`** / **Version**: Shows the version of Windows you are running.

- **`platform.win32_edition()`** / **Edition**: Shows the edition of Windows.

- **`platform.win32_is_iot()`** / **Is IoT / Is Embedded**: Shows whether or not your system is Windows IoT/Embedded (?)

#### Darwin info : `-d`, `--darwin`

This argument shows the output of `platform.mac_ver()`.

- **`platform.mac_ver()`** / **Mac Version**: Shows the version of macOS you are running.

#### iOS info : `-i`, `--ios`

> [!IMPORTANT]
> Not every Python version supports this argument.

This argument shows the output of `platform.ios_ver()`.

- **`platform.ios_ver()`** / **iOS Version**: Shows the version of iOS you are running.

#### Other info : `-o`, `--other`

This argument shows the output of `platform.java_ver()` and `platform.libc_ver()`.

#### Help : `-h`, `--help`

This argument shows help about how to use the script.
