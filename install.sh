#!/bin/bash
set -e

USER_NAME=$(whoami)
INSTALL_DIR="$(pwd)"

echo "[*] Installing system dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip build-essential cmake

echo "[*] Installing Python packages..."
pip3 install -r requirements.txt

SERVICE_FILE="/etc/systemd/system/sue.service"

echo "[*] Creating systemd service at $SERVICE_FILE"
sudo bash -c "cat > $SERVICE_FILE" <<EOF
[Unit]
Description=SUE Autonomous Assistant (llama.cpp)
After=network.target

[Service]
Type=simple
User=$USER_NAME
WorkingDirectory=$INSTALL_DIR
ExecStart=/usr/bin/python3 $INSTALL_DIR/sue.py
Restart=on-failure
RestartSec=3

[Install]
WantedBy=multi-user.target
EOF

echo "[*] Reloading systemd..."
sudo systemctl daemon-reload

echo "[*] Enabling SUE to start at boot..."
sudo systemctl enable sue.service

echo "[*] Starting SUE now..."
sudo systemctl start sue.service

echo "--------------------------------------------------"
echo " SUE (llama.cpp edition) is installed."
echo " Place your GGUF models as:"
echo "   $INSTALL_DIR/models/sue.gguf"
echo "   $INSTALL_DIR/models/embedding.gguf"
echo " Then restart SUE with:"
echo "   sudo systemctl restart sue"
echo "--------------------------------------------------"
