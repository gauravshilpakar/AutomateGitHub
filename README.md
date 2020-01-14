Automate Process of logging into your GitHub, creating a repository, setting up remote repository and pushing initial commits.

Note: Written in UTF-8 Encoding

---

To run the program:
* git clone https://github.com/gauravshilpakar/automate_git_py
* pip install PyGithub
* edit the <b>USERNAME</b> and <b>PASSWORD</b> field in the `script.py` file
* edit the <b>username</b> field in `github.bat` file as well


* <b>IMPORTANT:</b> add the folder containing the `github.bat` to the environment variable.
    * WIN key
    * type <b>env</b>
    * edit path in the lower System Variable tab
    * add new path to the folder
    
* CD into the existing project folder
* Run as `github` in CLI

# In Progress
## Initial Commits

 - [x] git init
 - [x] git remote add https://github.com/username/repo
 - [x] git add *
 - [x] git commit -m 'init commit'

## Newer Commits

 - [ ] git add * 
 - [ ] git commit -m 'commit message'  
 - [ ] git push origin master
![alt text](https://github.com/gauravshilpakar/automate_git_py/blob/master/img/Capture1.PNG)

![alt text](https://github.com/gauravshilpakar/automate_git_py/blob/master/img/Capture2.PNG)