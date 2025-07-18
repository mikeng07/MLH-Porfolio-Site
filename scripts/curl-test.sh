#!/bin/bash

# Generate random data
NAME="User_$RANDOM"
EMAIL="user${RANDOM}@example.com"
CONTENT="Hi there on $(date)"

# POST request to add a timeline post
echo "Posting new timeline post"
POST_RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post \
  -d "name=$NAME" \
  -d "email=$EMAIL" \
  -d "content=$CONTENT")



# GET request to fetch all timeline posts
echo "Fetching timeline posts"
GET_RESPONSE=$(curl -s http://127.0.0.1:5000/api/timeline_post)


# Check if the new name is in the GET response
echo "Checking if the new name was added..."
if echo "$GET_RESPONSE" | grep -q "$NAME"; then
  echo "New name: "$NAME" found!"
else
  echo "No new name found!"
fi