

```
jmeter -n -t <path-to-jmx-file> -l <path-to-csv-output-file> e -o <path-to-html-output-folder>  

jmeter -n -t /home/ec2-user/apache-jmeter-5.4.3/example/Sample.jmx -l /home/ec2-user/apache-jmeter-5.4.3/results/result.csv e -o /home/ec2-user/apache-jmeter-5.4.3/reports 

```

Or if you have .jtl file then use below command to generate html report

```
jmeter -g(path of .jtl file) -o(path of output folder where you want to save the results)

jmeter -g"/home/ec2-user/apache-jmeter-5.4.3/result.jtl" -o"/home/ec2-user/apache-jmeter-5.4.3/"
```
