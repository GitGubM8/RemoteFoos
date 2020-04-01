import os
import slack

client = slack.WebClient(token=os.environ['REMOTE_FOOS_TOKEN'])