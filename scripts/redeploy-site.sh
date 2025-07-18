#!/bin/bash

# kill all server
tmux kill-server

# go to porfolio directory
cd ~/MLH-Porfolio-Site

# get the latest change and ignored all uncommited
git fetch && git reset origin/main --hard

# start new detached tmux session
tmux new-session -d -s portfolio bash -c "source python3-virtualenv/bin/activate && pip install -r requirements.txt && flask run --host=0.0.0.0"

# confirm
echo "Redeployed"

