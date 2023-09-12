# Docker community support "We currently only provide packages for RHEL on s390x (IBM Z). Other architectures are not yet supported for RHEL, but you may be able to install the CentOS packages on RHEL. Refer to the Install Docker Engine on CentOS page for details."
# https://docs.docker.com/engine/install/centos/

          #!/bin/bash -xe
          echo 'Starting Update'
          sudo yum install -y yum-utils
          sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
          echo 'Create test file' 
          sudo mkdir /opt/scandir
          sudo chmod -R 777 /opt/scandir
          echo 'X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*' > /opt/scandir/bad.txt
          echo 'I am good file' > /opt/scandir/good.txt
          echo 'Install Docker Engine'
          sudo yum install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
          sudo systemctl start docker
          sudo docker run hello-world
          echo 'Install clamav image'
          sudo docker pull clamav/clamav:1.0.2
          sudo groupadd clamav
          echo 'Adding clamav user in group'
          sudo useradd -g clamav -s /bin/false -c "Clam Antivirus" clamav
          sudo chown -R clamav:clamav /var/lib/clamav/
          echo 'Running clamav'
          #sudo docker run -it --rm --name "clam_container" --mount source=clam_db, target=/var/lib/clamav --env 'CLAMAV_NO_FRESHCLAMD=true' clamav/clamav:stable
          #sudo docker run -it --rm --name "clam_container_01" clamav/clamav:1.0.2_base
          #sudo docker volume create clam_db
          #sudo docker run -it --rm --name "clam_container_01" --mount source=clam_db,target=/var/lib/clamav clamav/clamav:1.0.2_base
          sudo docker run --rm \
            --name "clamav_container_01" \
            --mount source=clam_db,target=/var/lib/clamav \
            --mount type=bind,source=/opt/scandir,target=/scandir \
            --env 'CLAMAV_NO_FRESHCLAMD=false' \
            --env 'FRESHCLAM_CHECKS=24' \
            clamav/clamav:1.0.2_base
          sudo docker run --rm \
            --name "clamav_container_02" \
            --mount source=clam_db,target=/var/lib/clamav \
            --mount type=bind,source=/opt/scandir,target=/scandir \
            --env 'CLAMAV_NO_FRESHCLAMD=true' \
            --env 'FRESHCLAM_CHECKS=24' \
            clamav/clamav:1.0.2_base \
            clamscan /scandir