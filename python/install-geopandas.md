### Install geopandas in Anaconda distribution.
#### I assume Anaconda is already installed. 

1. Open Anaconda command prompt
2. Check number of existing environment
   run >> conda env list

output should look like below 
(base) C:\Users\...>conda env list
base                  *  C:\ProgramData\Anaconda3

It means only one env 'base' exist. 

3. check python version
   run >> python --version
output will look like 'Python 3.7.6'

4. Now create a new environment. Example env name 'py37'
run >> conda create --name py37 python=3.7
output will look like below 
Collecting package metadata (current_repodata.json): done
Solving environment: done

5. Activate the environment 
run >> conda activate py37

6. run below command to install geopandas
conda install geopandas
Note: It may take few mins to process. So be patient
It will listup all supporting packages. 

Ultimately it will show "The following NEW packages will be INSTALLED:" followed by hundreds of packages. Just enter Y when it asks to proceed or not. 

During installation it may show "solving environment: failed with initial frozen solve. retrying with flexible solve. geopandas". Give it time to complete the process. 
