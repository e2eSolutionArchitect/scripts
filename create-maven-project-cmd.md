### check maven version

mvn --version

### Run below command in your command prompt

mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-app -DarchetypeArtifactId=maven-archetype-quickstart -DarchetypeVersion=1.4 -DinteractiveMode=false

### create a parent and child project

### parent project

mvn archetype:generate -DgroupId=com.mycompany.commonconfig -DartifactId=commonconfig-parent

### child project

cd commonconfig-parent

mvn archetype:generate -DgroupId=com.mycompany.commonconfig  -DartifactId=commonconfig-domain
