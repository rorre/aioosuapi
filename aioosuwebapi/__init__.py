import aiohttp
import html
import json


class aioosuwebapi:
    def __init__(self):
        # self._token = token
        self._base_url = "https://osu.ppy.sh/"

    async def _raw_request(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.get(self._base_url+endpoint) as response:
                response_text = (await response.text())
                if len(response_text) > 4:
                    return response_text
                else:
                    raise ValueError('Connection issues')

    async def get_contents_in_between(self, after, before, string):
        return ((string.split(after))[1].split(before)[0]).strip()

    async def get_beatmapset_discussions(self, beatmapset_id):
        http_contents = await self._raw_request('beatmapsets/%s/discussion' % (beatmapset_id))
        if "json-beatmapset-discussion" in http_contents:
            results = await self.get_contents_in_between('<script id="json-beatmapset-discussion" type="application/json">', '</script>', http_contents)
            return json.loads(results)
        elif "<h1>Page Missing</h1>" in http_contents:
            return {
                "beatmapset": {
                    "status": "deleted"
                }
            }
        else:
            raise ValueError('Endpoint has most likely been changed')

    async def get_group_members(self, group_id):
        http_contents = await self._raw_request('groups/%s' % (group_id))
        if "json-users" in http_contents:
            result = await self.get_contents_in_between('<script id="json-users" type="application/json">', '</script>', http_contents)
            return json.loads(result)
        else:
            raise ValueError('Endpoint has most likely been changed')
