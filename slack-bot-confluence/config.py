import os
from slack import WebClient
from slack.web.client import Future, SlackResponse
from typing import Union, Optional


class BotConfig:
    def __init__(self):
        CONFLUENCE_URI = "wiki/rest/api/content/search"
        QUERY_TYPE = "cql=text"

        self.slack = {
            "channel_id": os.environ["SLACK_CHANNEL_ID"],
            "api_token": os.environ["SLACK_API_TOKEN"],
            "secret": os.environ["SLACK_SIGNING_SECRET"],
        }

        self.confluence = {
            "url": "{}/{}?{}".format(
                os.environ["CONFLUENCE_URL"], CONFLUENCE_URI, QUERY_TYPE
            ),
            "user": os.environ["CONFLUENCE_USER"],
            "api_token": os.environ["CONFLUENCE_TOKEN"],
        }

    def get_slack_channel(self):
        return self.slack["channel_id"]

    def get_slack_token(self):
        return self.slack["api_token"]

    def get_slack_secret(self):
        return self.slack["secret"]

    def get_confluence_url(self):
        return self.confluence["url"]

    def get_confluence_user(self):
        return self.confluence["user"]

    def get_confluence_token(self):
        return self.confluence["api_token"]


class SlackService:
    def __init__(self) -> None:
        self.slack = WebClient(token=BotConfig.get_slack_token)
        self.channel_id = BotConfig.get_slack_channel

    def open_view(self, trigger_id: str, view: dict) -> Union[Future, SlackResponse]:
        return self.slack.views_open(trigger_id=trigger_id, view=view)

    def user_info(self, user_id: str) -> Union[Future, SlackResponse]:
        return self.slack.users_info(user=user_id)

    def ephemeral_message(
        self, user_id: str, text: str = None, blocks: str = None
    ) -> Optional[Union[Future, SlackResponse]]:
        if blocks is not None:
            return self.slack.chat_postEphemeral(
                user=user_id, channel=self.channel_id, blocks=blocks,
            )
        elif text is not None:
            return self.slack.chat_postEphemeral(
                user=user_id, channel=self.channel_id, text=text,
            )

        return None
