git pull

python main.py

timeout /t 5 /nobreak

git add .
git commit -m "update %date%"
timeout /t 5 /nobreak
git push
timeout /t 5 /nobreak
