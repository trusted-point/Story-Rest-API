
### 1. Update and install required packages
```bash
sudo apt update && sudo apt install python3 python3-venv git -y
```
### 2. Clone the repository
```bash
git clone https://github.com/trusted-point/Story-Rest-API.git
```
### 3. Activate virtual enviarment
```bash
cd Story-Rest-API
python3 -m venv venv
source venv/bin/activate
```
#### 4. Install dependencies
```bash
pip3 install -r requirements.txt
```
### 4. Start the app
Edit `config.yaml` with your desired parameters. 
It's important to specify correct Story rpc url (e.g. http://127.0.0.1:29659)
```bash
nano config.yaml
```
### 5. Start the app
```bash
uvicorn main:app --host 0.0.0.0 --port 8085 --workers 1
# Increasing the number of --workers allows the application to handle more concurrent requests
```
### 6. Start the app in background (Optional)
```bash
sudo tee /etc/systemd/system/story-rest-api.service > /dev/null <<EOF
[Unit]
Description=Story REST API
After=network.target
WorkingDirectory=$HOME/Story-Rest-API

[Service]
User=$USER
Type=simple
ExecStart=$(which uvicorn) main:app --host 0.0.0.0 --port 8085 --workers 1
Environment="CONFIG_PATH=$HOME/Story-Rest-API/config.yaml"
Environment="LOGPATH=$HOME/Story-Rest-API/logs/logs.log"
Environment="PYTHONPATH=$HOME/Story-Rest-API"
Restart=on-failure

[Install]
WantedBy=multi-user.target
EOF
```
```bash
sudo systemctl daemon-reload && \
sudo systemctl enable story-rest-api && \
sudo systemctl start story-rest-api
```
```bash
sudo journalctl -u story-rest-api -f -o cat
```
