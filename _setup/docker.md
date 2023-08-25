
```
FROM jupyter/scipy-notebook:29f53f8b9927

USER $NB_USER

# Install TensorFlow: 
RUN pip install tensorflow==2.2.0rc3

# Install PyTorch:
RUN pip install torch==1.4.0

```
