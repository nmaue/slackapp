# Slack App POC

This is a small POC I made to show my boss how we could use a custom app in Slack

Right now it just uses a slash command with a ticket number and returns the full link to our Request Tracker instance

Hoping to add more functionality eventually

## Installation
1. Install nginx and virtualenv
2. Clone repo to /opt/slackapp
3. cd /opt/slackapp
4. virtualenv venv
5. Install the requirements
6. Copy etc/slackapp.service to systemd folder
7. Enable and start the slackapp service
8. copy etc/slackapp.conf to the nginx configs
9. Enable and start nginx
