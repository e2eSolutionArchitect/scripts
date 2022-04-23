### No module named 'plotly.express'

Simply running 

conda install plotly 

didnt resolve my plotly.express error. 

If you are using conda just run below command. 

conda install -c plotly plotly=4.8.1

Note: Run this in other than 'base' environment. 

if you are at base env. change to another environment like 

conda activate <env-name>
  
then run plotly install command. 
