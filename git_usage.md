git init
git add .
git commit -m "message"# PAI
python artificial intelligent test


git branch

git checkout localbranch
git checkout -b newbranchname or git branch -M main, create local main branch 

git remote -v
git remote add new-origin https://github.com/yourusername/new-repository-name.git
git remote remove origin
git remote set-url origin https://github.com/yourusername/new-repository-name.git

git push -u origin localbranch
git push

git fetch origin

git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

git clone https://github.com/yourusername/new-repository-name.git




Client:
git init, generate .git file as local repository
git add filename (-A add all files in current fold), stag, git reove, unstage
git commit

git branch -M main, create local main branch 

ssh-keygen -t ed25519 -C "carson135@gmail.com"
    create two files at ~/.ssh/, 
    update ~/.ssh/config file, add 
      Host *
        AddKeysToAgent yes
        IdentityFile ~/.ssh/id_ed25519
        
    put pub key to github settting key filed
 
 ssh -T git@github.com  (ssh connected through ~/.ssh/config IdentityFile email and username configuration )

git remote add origin git@github.com:carson135/PAI.git (url of the project on github site, origin as the abr name)

