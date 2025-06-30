import os

from app.agent.god import GodAgent


class ArcGabriel(GodAgent):
    """Arcangel responsible for user communication via Telegram."""

    name: str = "arc_gabriel"
    description: str = "Handles user interaction channels"

    telegram_token: str = os.getenv("TELEGRAM_TOKEN", "")
