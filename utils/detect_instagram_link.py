import re
import asyncio

# 1️⃣ Full URLs
INSTAGRAM_URL_PATTERN = re.compile(
    r'(?:https?:\/\/)?(?:www\.|dd)?instagram\.com\/(?:p|reel|tv)\/([A-Za-z0-9_-]{5,})',
    re.IGNORECASE
)

# 2️⃣ Domain + ID (space-separated)
INSTAGRAM_SPACE_PATTERN = re.compile(
    r'(?:(?:www\.|dd)?instagram\.com\s+([A-Za-z0-9_-]{5,})|([A-Za-z0-9_-]{5,})\s+(?:www\.|dd)?instagram\.com)',
    re.IGNORECASE
)

# 3️⃣ “instagram” word + ID (space-separated)
INSTAGRAM_KEYWORD_PATTERN = re.compile(
    r'(?:(?:instagram)\s+([A-Za-z0-9_-]{5,})|([A-Za-z0-9_-]{5,})\s+(?:instagram))',
    re.IGNORECASE
)


def detect_instagram_link(text: str):
    """Detect valid Instagram video ID or URL in text."""
    if "instagram" not in text.lower():
        return None  # Not an Instagram-related message

    # 1. Full URL
    m1 = INSTAGRAM_URL_PATTERN.search(text)
    if m1:
        return {
            "type": "url",
            "video_id": m1.group(1),
            "match": m1.group(0)
        }

    # 2. Domain + ID
    m2 = INSTAGRAM_SPACE_PATTERN.search(text)
    if m2:
        video_id = next((g for g in m2.groups() if g), None)
        return {
            "type": "space",
            "video_id": video_id,
            "match": m2.group(0)
        }

    # 3. "instagram" + ID
    m3 = INSTAGRAM_KEYWORD_PATTERN.search(text)
    if m3:
        video_id = next((g for g in m3.groups() if g), None)
        return {
            "type": "keyword",
            "video_id": video_id,
            "match": m3.group(0)
        }

    return None


async def detect_instagram_link_async(text: str):
    return await asyncio.to_thread(detect_instagram_link, text)
