import instaloader
from instaloader import Post
import asyncio

loader = instaloader.Instaloader()

loader.context.log("Login...")
loader.load_session_from_file("07.abdulkhafizov")


async def download_instagram_video(video_id: str) -> str | None:
    def _download_sync() -> str | None:
        try:
            post = Post.from_shortcode(loader.context, video_id)

            return {
                "caption": post.caption[:300] + '...' if len(post.caption) > 300 else post.caption,
                "video": post.video_url,
                "cover": post.url
            }

        except Exception as e:
            return None

    return await asyncio.to_thread(_download_sync)
