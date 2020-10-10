echo -e "installing"
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install twilio
cd /data/data/com.termux/files/home/REDNET/__pycache__
python whatsapp.py
