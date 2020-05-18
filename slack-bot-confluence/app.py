from slack import WebClient
from flask import Flask
from flask import request
from flask import make_response
from slackeventsapi import SlackEventAdapter
from config import BotConfig, SlackService

import json
import requests

app = Flask(__name__)
# executor = Executor(app)

bot_config = BotConfig()
slack = SlackService()

slack_events_adapter = SlackEventAdapter(
    bot_config.get_slack_secret, "/slack/events", app
)

slack_web_client = WebClient(token=bot_config.get_slack_token)


@app.route("/search-confluence", methods=["POST"])
def search_confluence():
    payload = request.form.to_dict()

    FULL_URL = "{}~{}".format(bot_config.get_confluence_url, payload["text"].strip())

    response = requests.get(
        FULL_URL, auth=(bot_config.get_confluence_user, bot_config.get_confluence_token)
    )

    # Create blocks from requests.get
    # Successful response, let's parse the response payload so we can work with it later on
    if response.status_code == "200":
        with open("slack-bot-confluence/views/result-display.json") as json_file:
            data = json.load(json_file)

        slack.open_view(trigger_id=payload["trigger_id"], view=data)
        # slack chat_postEphermal message with top 5 results in a block
    # Something done fucked up. We will return the error to the user via Slack
    else:
        pass
        # slack chat_postEpheraml message indicating no results found

    return make_response("", 200)


# def compose_slack_block():


# def return_confluence_results():
# placeholder


def main():
    print("hello world!")


if __name__ == "__main__":
    main()
