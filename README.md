# Towards Understanding Third-party Library Dependency in C/C++ Ecosystem

## Dataset
All extracted dependencies
https://figshare.com/articles/dataset/repo2dep_json/19752820

##  CCScanner
This is a temporary repository to meet the Anonymous Review Policy. You can start the trial by running "scanner.py". 

Since Gitsubmodule and Buck module need some active tokens, such as GitHub token. We comment these modules in this anonymous version. You can still read the code.

Centris is available at: https://github.com/WOOSEUNGHOON/Centris-public.

### Install
CCScanner is written using Python3.
Install dependencies.
```·
pip install json5 bs4
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

