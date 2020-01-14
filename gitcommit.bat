@ECHO on

git add *
git commit -m " %~1% "
git push origin master

echo Committing changes...
echo Commit message: %~1%  