# simple-img-rec
A python library implementing cv2 as a simple template image recognition tool


## Usage
### Command line
```
pip install simple-img-rec

simrec /path/to/image /path/to/template
$ (x,y)
```

### Pyhton use
```
pip install simple-img-rec

>>> from simple-img-rec import detect_template
>>> detect_template('/path/to/image','/path/to/template')
(x,y)
```