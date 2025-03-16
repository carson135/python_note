git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

git clone https://github.com/yourusername/new-repository-name.git

git init
git add .
git commit -m "message"# PAI
git push # upload from local default branch to remote repository branch
git push -u origin localbranch #upload local specific branch

git pull #use the default configured remote and branch
git pull origin branch-name

git fetch #to see what changes would be pulled before actually pulling them
git fetch origin

git branch
git branch -r/-a
git branch -vv
git remote show origin  #show remote repository url and all branches

git checkout localbranch #change local branch
git checkout -b newbranchname or git branch -M main #create local new branch 

git remote -v #show remote repository url of fetch and push
git remote add new-origin https://github.com/yourusername/new-repository-name.git
git remote remove origin
git remote set-url origin https://github.com/yourusername/new-repository-name.git

Client:
git init, generate .git file as local repository
git add filename #-A add all files in current fold
git commit

ssh-keygen -t ed25519 -C "carson135@gmail.com"
    create two files at ~/.ssh/, 
    update ~/.ssh/config file, add 
      Host *
        AddKeysToAgent yes
        IdentityFile ~/.ssh/id_ed25519
        
    put pub key to github settting key filed
 
 ssh -T git@github.com  (ssh connected through ~/.ssh/config IdentityFile email and username configuration )

git remote add origin git@github.com:carson135/PAI.git (url of the project on github site, origin as the abr name)

# Remove file from githubrepository but keep it locally
git rm --cached path/to/your/file
git commit -m "Remove file from repository but keep it locally"
git push origin main
