import aiohttp
import json
from bs4 import BeautifulSoup


class aioosuwebapi:
    def __init__(self):
        self._base_url = "https://osu.ppy.sh/"

    async def _raw_request(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._base_url+endpoint) as response:
                response_text = (await response.text())
                if len(response_text) > 4:
                    return response_text
                else:
                    raise ValueError("Connection issues")

    async def get_beatmapset_discussions(self, beatmapset_id):
        http_contents = await self._raw_request(f"beatmapsets/{beatmapset_id}/discussion")
        if "json-beatmapset-discussion" in http_contents:
            soup = BeautifulSoup(http_contents, "html.parser")
            results = soup.find(id="json-beatmapset-discussion").string.strip()
            return json.loads(results)
        elif "<h1>Page Missing</h1>" in http_contents:
            return {
                "beatmapset": {
                    "status": "deleted"
                }
            }
        else:
            raise ValueError("Endpoint has most likely been changed")

    async def get_latest_ranked_beatmapsets(self):
        http_contents = await self._raw_request("beatmapsets")
        if "json-beatmaps" in http_contents:
            soup = BeautifulSoup(http_contents, "html.parser")
            results = soup.find(id="json-beatmaps").string.strip()
            return json.loads(results)
        else:
            raise ValueError("Endpoint has most likely been changed")

    async def get_group_members(self, group_id):
        http_contents = await self._raw_request(f"groups/{group_id}")
        if "json-users" in http_contents:
            soup = BeautifulSoup(http_contents, "html.parser")
            result = soup.find(id="json-users").string.strip()
            return json.loads(result)
        else:
            raise ValueError("Endpoint has most likely been changed")

    async def get_user(self, user_id):
        http_contents = await self._raw_request(f"users/{user_id}")
        if "json-user" in http_contents:
            soup = BeautifulSoup(http_contents, "html.parser")
            results = soup.find(id="json-user").string.strip()
            return json.loads(results)
        elif "<h1>User not found! ;_;</h1>" in http_contents:
            return None
        else:
            raise ValueError("Endpoint has most likely been changed")
