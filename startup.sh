# #!/bin/bash
# echo $WORKSPACE
# echo $GIT_CHECKOUT_DIR

# sudo apt-get update
# sudo apt-get install -y python3 
# sudo apt-get install -y python3-venv 
# sudo apt-get install -y python3-pip
# cd $WORKSPACE
# ls -lah
# sudo cp -r $WORKSPACE /opt/jenkins
# sudo chown -R jenkins /opt/jenkins

# cd /opt/jenkins
# python3 -m venv venv
# source venv/bin/activate
# pip3 install -r requirements.txt
 
# sudo systemctl restart cggpp

#!/bin/bash 
sudo apt update
sudo apt-get install python3-venv
python3 -m venv venv
cd $WORKSPACE
ls -lah
sudo cp -r $WORKSPACE /opt/jenkins
sudo chown -R jenkins /opt/jenkins
source venv/bin/activate
pip3 install -r requirements.txt
#python3 /opt/jenkins/cggpp-project/app.py
pytest -v /opt/jenkins/cggpp-project/

sudo chown -R jenkins /opt/jenkins
sudo systemctl daemon-reload
echo "systemctl daemon-reloaded"
sudo systemctl stop cggpp.service
echo "systemctl cggp.service stopped"
sudo systemctl start cggpp.service
echo "systemctl cggp.service has started"