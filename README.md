git init
git add .
git commit -m "message"


git branch

git checkout localbranch
git checkout -b newbranchname

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
