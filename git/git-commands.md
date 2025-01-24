

### create new branch from another

```
git checkout -b new-branch old-branch;
git push --set-upstream origin new-branch;
```
### checkout a branch

```
git checkout branchname
```

### Merge code from feature branch 'dev-branch' to master

```
 git add –A
 git commit –m "Some commit message"
 git checkout master
Switched to branch 'master'
 git merge dev-branch  (this is to merge changes from dev-branch to master)
git push (push changes in master branch)
```

### Get the update from a branch that is ahead of your branch. 

```
# branch A is a feature branch which is behind of 'main' branch. Here is how to take updates from main TO branch A

git checkout branch-A
git pull
git merge origin/main
git add .
git commit -m "updated with main branch"
git push
```


### git commit history 

```
git log --pretty=oneline
```

### delete branch locally
```
git branch -d localBranchName
```
### delete branch remotely
```
git push origin --delete remoteBranchName
```
### The command to list all branches in local and remote repositories is:
```
git branch -a
```
### If you require only listing the remote branches from Git Bash then use this command:
```
git branch -r
```

### You may also use the show-branch command for seeing the branches and their commits as follows:
```
git show-branch
```
### If you want to rename a branch while pointed to any other branch
```
git branch -m oldname newname
```
### If you want to rename the current branch
```
git branch -m newname
```
### list content 
```
ls - ltrh 
```
### Create tag

1. checkout the branch first where you want to create the tag
2. After that create tag and and push. Follow below commands in sequence 

consider our tag name as 'release-v1.0'
```
- git checkout <branch name>
- git tag <tag name> . e,g. git tag release-v1.0 
- git tag -a release-v1.0 -m "add comments"   use it while adding comments with tag
- git push --tags
```

Delete a tag 
```
 git tag -d <tag name>
``` 
 push a tag from local to origin branch 
 
``` 
 git push origin -d release-v1.0
```

