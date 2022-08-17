# Towards Understanding Third-party Library Dependency in C/C++ Ecosystem

## Dataset
All extracted dependencies and ground truth are available at: https://figshare.com/s/9e2fd7a1389af8266bfe

Detection targets can be downloaded from official GitHub repositories or official websites.
##  CCScanner
This is a temporary repository to meet the Anonymous Review Policy. You can try to use it by running "scanner.py" or install the pip package "ccscanner".

Centris is available at: https://github.com/WOOSEUNGHOON/Centris-public.

results.json contains the extracted dependencies from "tests/test_data".

### Install
CCScanner is written using Python3.
Install dependencies.
```·
pip install json5 bs4 GitPython lxml
```

### Usage
run command:
```
cd ccscanner
python ccscanner/scanner.py -d $directory_to_scan -t $results_json_file
```
All results will be saved to a json files. The default path to save results is ```./results.json```.

```Deps``` field in results is all extracted dependencies.

### Pip package
We have released a pip package. You can try to use it.

```
pip install ccscanner
$ ccscanner_print -d ${directory to scan} -t ${file to save}
```

### Test
```tests``` directory contains some configuration files in real-world applications to test CCScanner.

CCScanner will be continuously maintained in future. It is welcomed if you have any issues or want to join us to improve it.

