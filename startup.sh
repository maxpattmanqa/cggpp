#!/bin/bash
echo $WORKSPACE
echo $GIT_CHECKOUT_DIR

sudo apt-get update
sudo apt-get install -y python3 
sudo apt-get install -y python3-venv 
sudo apt-get install -y python3-pip
cd $WORKSPACE
ls -lah
sudo cp -r $WORKSPACE /opt/jenkins
sudo chown -R jenkins /opt/jenkins

cd /opt/jenkins
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
 
sudo systemctl restart cggpp