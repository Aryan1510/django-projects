
echo " BUILD START"
python3.11.9  -m pip install -r requirements.txt
python3.11.9 manage.py collectstatic  --noinput --clear
echo " BUILD END"