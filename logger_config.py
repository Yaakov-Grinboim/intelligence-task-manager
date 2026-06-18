import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] | %(levelname)s | %(massage)s",
    handlers=[logging.StreamHandler(), logging.FileHandler(".\logs\app.log", "a")],
)

logger = logging.getLogger(__name__)
