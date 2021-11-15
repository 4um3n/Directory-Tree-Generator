# Directory Tree Generator
Simple program to generate tree of a given directory.

## Screenshots

![](https://github.com/4um3n/Directory-Tree-Generator/blob/main/Screenshots/DTG.png)
![](https://github.com/4um3n/Directory-Tree-Generator/blob/main/Screenshots/DTG1.png)
![](https://github.com/4um3n/Directory-Tree-Generator/blob/main/Screenshots/DTG2.png)
![](https://github.com/4um3n/Directory-Tree-Generator/blob/main/Screenshots/DTG3.png)


## Installation
1. Clone the repo: `git clone https://github.com/4um3n/Directory-Tree-Generator.git`

## Usage
### CLI version:
1. Open cloned repository and execute: `python3 tree.py /Path/To/Desired/Directory`
2. These are the available options:

```
usage: tree [-h] [-v] [-f [OUTPUT_FILE]] [-d] [ROOT_DIR]

'Directory Tree', a directory tree generator

positional arguments:
  ROOT_DIR              Generate a full directory tree starting at ROOT_DIR

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -d, --dir-only        ignore files and get only directories
  -f [OUTPUT_FILE], --file [OUTPUT_FILE]
                        Store the generated tree to file in markdown format

```

### GUI version
1. Open cloned repository and execute `python3 tree_gui.py` 

## Dependencies
### tkinter
Install on Debian and Debian like GNU/Linux distros: `apt-get install python3-tk`

Install on Arch and Arch like GNU/Linux distros: `pacman -S tk`

Install on Fedora `dnf install python3-tkinter`


## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
```
https://www.apache.org/licenses/LICENSE-2.0
```
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
