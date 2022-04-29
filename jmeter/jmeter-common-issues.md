
## Error in NonGUIDriver Following remote engines could not be configuied: [10.#.#.#,10.#.#.#]

### Possible causes:
- Jmeter is not installed properly in worker nodes. check by running 'jmeter --version'
- check cloud-init-output file log
```
sudo cat /var/log/cloud-init-output.log
```
- worker nodes configuration must be enough to run jmeter. e.g, in AWS EC2 t2.micro cant hold jmeter. recommended to use t2.small onwards

## Stuck at configuring remote engine: 10.#.#.#
- check the firewall or security group. it is basically restricting inboud traffic to worker nodes. 
