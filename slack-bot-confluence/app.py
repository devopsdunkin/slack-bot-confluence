from slack import WebClient
from flask import Flask
from flask import request
from flask import make_response
from slackeventsapi import SlackEventAdapter

import os
import json
import requests

app = Flask(__name__)
# executor = Executor(app)

slack_events_adapter = SlackEventAdapter(
    os.environ["SLACK_SIGNING_SECRET"], "/slack/events", app
)

slack_web_client = WebClient(token=os.environ["SLACK_API_TOKEN"])

# Variables that we do not need to change
URI = "wiki/rest/api/content/search"
QUERY = "cql=text"
BASE_URL = os.environ["CONFLUENCE_URL"].rstrip("/")


@app.route("/search-confluence", methods=["POST"])
def search_confluence():
    trigger_id = request.form.get("trigger_id")
    search_criteria = request.form.get("text")

    # Need to grab the payload and get the text to search for

    FULL_URL = "{}/{}?{}~{}".format(BASE_URL, URI, QUERY, search_criteria)

    response = requests.get(FULL_URL, auth=(os.environ["CONFLUENCE_USER"], os.environ["CONFLUENCE_PASS"]))

    # Create blocks from requests.get
    if response is not None:
        # slack chat_postEphermal message with top 5 results in a block
    else:
        # slack chat_postEpheraml message indicating no results found

    return make_response("", 200)


def main():
    print("hello world!")


if __name__ == "__main__":
    main()
