import httpx
import logging

from .config import settings

logger = logging.getLogger(__name__)


async def user_started_private_chat(user_id: int or str) -> bool:
    """
    True, if user started the bot (private-chat exists).
    """
    url = (
        f"{settings.telegram_api_url}/bot{settings.bot_token}/getChat"
        f"?chat_id={user_id}"
    )
    async with httpx.AsyncClient(timeout=2) as client:
        try:
            resp = await client.get(url)
            data = resp.json()
            return bool(data.get("ok"))
        except Exception as exc:
            logger.warning("Telegram check failed for %s: %s", user_id, exc)
            return False
