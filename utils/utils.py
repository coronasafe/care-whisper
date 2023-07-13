
import aiohttp
import uuid

from base import ROOT_DIR


async def adownload_audio_file(url):

    file_path = f'{str(ROOT_DIR)}/audios/{str(uuid.uuid4())}.mp3'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            audio_file = await response.read()
            with open(file_path, 'wb') as f:
                f.write(audio_file)

    return file_path