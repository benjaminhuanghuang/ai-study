# Machine Learning Study Project

## Setup
```
    $ brew install python3
    
    $ virtualenv --system-site-packages -p python3 venv3
    
    $ . venv3/bin/activate
    (venv3)$ pip3 install -r requirements.txt

    ...
    (venv3)$ deactivate
```


## Add python kernal to jupyter
```
    python -m ipykernel install --user --name other-env --display-name "Python 3"
```