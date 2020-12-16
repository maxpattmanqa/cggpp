#!/bin/bash
sudo apt-get install -y python3-pip
cd $WORKSPACE
ls -lah
sudo cp -r $WORKSPACE /opt/jenkins
sudo chown -R jenkins /opt/jenkins

cd /opt/jenkins 
python3 -m venv venv
ls -lah
cd ..
source venv/bin/activate
pip3 install -r requirements.txt

sudo systemctl daemon-reload
sudo systemctl stop cggpp.service
sudo systemctl start cggpp.service