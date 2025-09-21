@echo off
echo Starting GitHub deployment...

git init
git branch -M main
git add .
git commit -m "Initial commit - Basketball Tracking Analytics v1"
git remote add origin https://github.com/wa1thyy/basketball-tracking-analytics.git
git push -u origin main

echo Done! Project uploaded to GitHub.
pause
