
```
python3 -V
python -version

python3 <filename.py>
python3 demo.py
```

**Create Virtual Python Environment using Windows command prompt**

```
python --version
# OR
python3 -V

C:\ mkdir pyenv
C:\ cd pyenv
C:\pyenv> python -m venv <env-name>
C:\pyenv> python -m venv py310
C:\pyenv> .\py310\Scripts\activate
(py310) c:\pyenv> pip install jupyter
(py310) c:\pyenv> jupyter notebook

# Similarly install any other libs you need.
pip install monai==1.3.0 torch==2.0.1 pydicom==2.4.4 opencv-python==4.8.0.76 numpy==1.23.5
```

***list python packages***

```
pip list
```

**Check anaconda env list

```
conda env list
** activate a conda env
conda activate env_name
```

** Remove : 
```
conda remove --name myenv --all
```

***To create an environment with a specific version of Python***
```
conda create --name myenv python=3.7
```
OR 
```
conda create --name myenv
```

***Clone*** 
```
conda create --name new_env --clone myenv
```
