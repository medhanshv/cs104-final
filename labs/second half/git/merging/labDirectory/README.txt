In the scripts folder, you will find 3 scripts present :-

reset.sh :- For initializing the activity and creating the working_directory folder, and also
            for resetting everything to scratch if you mess something up.

submit.sh :- Run this script before submitting. Submitting without running this script may lead
             to problems with git.

reopen.sh :- If you wish to continue work from where you left off, after running submit.sh, use
             reopen.sh. It brings you to the same state from where you submitted.

***PLEASE USE RESET.SH WITH CAUTION IT CAN ERASE ALL YOUR PROGRESS IF FILES HAVE NOT BEEN COMMITTED ON GIT VCS****

To run each script, first navigate to the scripts folder using the cd command.
Then run the command bash <script_name>.sh

Navigate to scripts/ and run bash reset.sh to begin the activity.


************* EXTRA INFO *************
----Git Errors---- 

After initializing the git repo inside a git repository, you may run into some error about dubious ownership of the directory.

To avoid this run the following command:-

git config --global --add safe.directory /home/labDirectory/working_directory

This is because we have created a git repo inside another git repo, which is a security issue for git.
There is a very interesting reason why git has this feature, for those who are interested feel free to
read up here :- https://github.blog/2022-04-12-git-security-vulnerability-announced/#cve-2022-24765

Also, when you try to commit, the repo will ask for your username and email. 
Another security feature which ensures that no unknown person can commit to the repository.

To resolve this run the following commands :- 

git config user.email "<email ID>"
git config user.name "<name>"

Eg. 

git config user.email "student.iitb.ac.in"
git config user.name "student"
