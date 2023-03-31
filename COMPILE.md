# Compile binary

In order to execte the command, you must compile the python source code to get a binary executable file.
To do so,  use [pyinstaller](https://pyinstaller.org/en/stable/).

## Run pyinstaller

Use this command to compile the python source code:

```bash
pyinstaller ./src/main.py --onefile --name cimg
```

This create a directory called `dist/` where the binary file is saved.
