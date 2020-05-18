from slack import WebClient
from slack.web.client import Future, SlackResponse
from config import BotConfig
from typing import Union, Optional


class SlackService:
    def __init__(self) -> None:
        self.slack = WebClient(token=BotConfig.SLACK_API_TOKEN)
        self.channel_id = BotConfig.SLACK_CHANNEL_ID

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