## To create
just follow the github instructions

```
echo "# Metaheuristic_optimisation" >> README.md # Start repository with a README
git init
git add README.md # can also "git add -A" if there are already files in the folder 
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/lollcat/repository.git      
git push -u origin main
```

# Add a new feature branch
```
echo "# Metaheuristic_optimisation" >> README.md
git init
git add README.md # can also "git add -A" if there are already files in the folder 
git commit -m "first commit"
git branch -M feature_branch_name
git remote add origin https://github.com/lollcat/repository.git      
git push -u origin feature_branch_name
```


## Clone a single branch
git clone **url** --branch **branch** --single-branch **local_folder**
                

## Once created
```
git add -A # add files
git commit -m "This is the commit message"
git push
```

## To ignore a folder
Make a file called .gitignore and type the folder path as such:
```
folder_to_ignore/
```

## Pull overwriting local where different
```
# https://stackoverflow.com/questions/1125968/how-do-i-force-git-pull-to-overwrite-local-files
git reset --hard HEAD   
git pull
```
