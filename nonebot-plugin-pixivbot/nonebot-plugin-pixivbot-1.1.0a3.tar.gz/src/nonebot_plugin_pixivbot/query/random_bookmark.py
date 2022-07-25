from lazy import lazy
from nonebot import on_regex
from nonebot.adapters import Bot, Event
from nonebot.matcher import Matcher
from nonebot.typing import T_State

from nonebot_plugin_pixivbot.config import Config
from nonebot_plugin_pixivbot.global_context import context
from nonebot_plugin_pixivbot.handler.common import RandomBookmarkHandler
from .query import Query, register_query
from .utils import get_count, get_common_query_rule, get_post_dest


@register_query(context)
class RandomBookmarkQuery(Query):
    conf = context.require(Config)

    def __init__(self):
        super().__init__()
        self.handler = context.require(RandomBookmarkHandler)

    @lazy
    def matcher(self):
        return on_regex("^来(.*)?张私家车$", rule=get_common_query_rule(), priority=5)

    async def on_match(self, bot: Bot, event: Event, state: T_State, matcher: Matcher):
        await self.handler.handle(count=get_count(state), post_dest=get_post_dest(bot, event))
