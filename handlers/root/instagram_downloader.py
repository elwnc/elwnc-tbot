from router import router
from aiogram import F
from aiogram.types import Message, InputFileUnion
from utils.detect_instagram_link import detect_instagram_link, detect_instagram_link_async
from utils.download_instagram_video import download_instagram_video


@router.message(F.text.cast(detect_instagram_link))
async def instagram_download_handler(m: Message):
    timer = await m.answer("<b>Video yuklanmoqda</b>\n<i>Iltimos, biroz kutib turing...</i>")
    
    # Bu yerda video ID kelishi aniq, sababi biz oldindan vidoe ID kelishiga tekshirib olyabmiz
    link_data = await detect_instagram_link_async(m.text)
    video_data = await download_instagram_video(link_data['video_id'])

    if video_data:
        await m.answer_video(**video_data)
        await timer.delete()
    else:
        await timer.edit_text("Uzur, ushbu videoni yuklab olib bo'lmaydi.")
