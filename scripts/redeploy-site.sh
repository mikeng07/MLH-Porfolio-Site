#!/bin/bash

# go to porfolio directory
cd ~/MLH-Porfolio-Site

# get the latest change and ignored all uncommited
git fetch && git reset origin/main --hard

# start new detached tmux session
tmux new-session -d -s portfolio bash -c "source python3-virtualenv/bin/activate && pip install -r requirements.txt "

# restart myportfolio service
systemctl restart myportfolio

# confirm
echo "Redeployed"

