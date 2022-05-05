Pull docker image 
#### Refer: https://hub.docker.com/r/justb4/jmeter

```
docker pull justb4/jmeter
```
Check pulled image

```
docker images
```

Tag the image with a handy nick name

```
docker tag justb4/jmeter jmeter
```

Run jmeter on docker

```
docker run jmeter
```
you will get X11 display error as we are using cli mode only. there is no GUI.  The goal is to run the jmeter in cli mode. so ignore the error for now.

Now run 
```
# For Single Node
docker run jmeter -n -t /opt/apache-jmeter-5.4.3/bin/examples/CSVSample.jmx -l results.jtl -Dserver.rmi.ssl.disable=true

# mount the source to get the jmeter result in your target
docker run --mount type=bind, source="mnt/c/tools/apache-jmeter-5.4.3/bin/", target="/opt/apache-jmeter-5.4.3/bin" jmeter -n -t bin/example.jmx -l bin/results.jtl -Dserver.rmi.ssl.disable=true

For Distributed load test
docker run -n -t /opt/apache-jmeter-5.4.3/bin/examples/CSVSample.jmx -l results.jtl -R <worker-node-privateIp1,privateIp1> -Dserver.rmi.ssl.disable=true
```
