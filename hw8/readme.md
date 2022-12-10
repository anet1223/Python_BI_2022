# UNIX programs in Python

This folder contains some scripts that imitate Unix command in terminal. Scripts run without additional libraries. NB: don't use python version 3.10 or higher.

## Installation

1.  Copy folder with scripts:

```{bash}
git clone https://github.com/anet1223/Python_BI_2022/tree/hw8/hw8
```

2.  Create virtual environment

```{bash}
python -m venv okr
```

3.  Activate virtual environment

```{bash}
source okr/Scripts/activate
```

4.  Try commands according their functions

**ls. py** print list of files in the directory. Takes path to the folder. Optional argument '-a' allows to see hidden files that start with dot. Example:

```{bash}
$ ./ls.py
1.txt
cat.py
```

```{bash}
$ ./ls.py -a
.
..
.test.txt
1.txt
cat.py
```

**cat.py** print file content. Takes path to the file or files. Otherwise, takes stdin. Example:

```{bash}
$ ./cat.py 1.txt
а
я
иду
шагаю
шагаю
шагаю
по Москве
```

**tail.py** print number of lines from the end of the file. Takes path to the file or files. Otherwise, takes stdin. As default print 10 lines. This could be change by argument with desired number of lines. Example:

```{bash}
$ ./tail.py -3 1.txt
шагаю
шагаю
по Москве
```

**uniq.py** print file content and omit repeated lines. Takes path to the file. Otherwise, takes stdin. Example:

```{bash}
$ ./uniq.py 1.txt
а
я
иду
шагаю
по Москве
```

**sort.py** sort lines in alphabetical order. Takes path to the file. Otherwise, takes stdin. Example:

```{bash}
$ ./sort.py 1.txt
а
иду
по Москве
шагаю
шагаю
шагаю
я
```

**wc.py** count lines (argument -l), words (argument -w) or bytes (argument -c). Takes path to the file. Otherwise, takes stdin. Example:

```{bash}
$ ./wc.py -l -w -c 1.txt
6 8 69 1.txt
```

**rm.py** remove file or directory (with argument -r). Takes path to file or directory (only with -r). Example:

```{bash}
$ ./rm.py folder/1.txt
$ ./rm.py -r folder/
```
