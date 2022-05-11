### export and import docker image.
#### Somtime we need to copy docker image from one VM to another VM. follow below steps for export and import

### save/export docker image to tar file
```
docker save -o ./dkr-test.tar dkr-image-name:latest
```

copy the tar file to another VM and import there. 'myimage:1.0.0' is new name there
[Click here](https://github.com/e2eSolutionArchitect/scripts/blob/main/aws/ec2/upload-file-ec2-s3.md) for how to copy

```
docker import ./dkr-test.tar myimage:1.0.0
```
