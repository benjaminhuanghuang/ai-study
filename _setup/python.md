## Setup virtual environment
```
$ python3 -m venv venv3

$ . venv3/bin/activate
or
> .\venv3\Scripts\activate.bat                # windows
> .\venv3\Scripts\Activate.ps1                # windows

(venv3)$ pip3 install -r requirements.txt


(venv3)$ python3 -m notebook
...
(venv3)$ deactivate
```


## Add python kernal to jupyter
```
    python -m ipykernel install --user --name other-env --display-name "Python 3"
```

## Open ipynb in VS code
Set Kernel to venv3
