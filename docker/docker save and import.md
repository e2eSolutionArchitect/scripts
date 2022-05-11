### export and import docker image.
#### Sometime we need to copy docker image from one VM to another VM. follow below steps for save and load

### save/export docker image to tar file
```
docker save -o ./dkr-test.tar dkr-image-name:latest
```

copy the tar file to another VM and import there. 'myimage:1.0.0' is new name there
[Click here](https://github.com/e2eSolutionArchitect/scripts/blob/main/aws/ec2/upload-file-ec2-s3.md) for how to copy

```
docker load < ./dkr-test.tar

after loading check your image list the new image should be there
```
NOTE: if you user docker import in this case you will get error. if you use SAVE and user LOAD to import
