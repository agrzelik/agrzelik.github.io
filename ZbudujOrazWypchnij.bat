git pull

python main.py

timeout /t 2 /nobreak

git add .
git commit -m "update %date%"
timeout /t 2 /nobreak
git push
timeout /t 2 /nobreak
