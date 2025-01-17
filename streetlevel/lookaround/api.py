import requests
from aiohttp import ClientSession
from requests import Session

from streetlevel.lookaround.proto import MapTile_pb2


COVERAGE_TILE_ENDPOINT = "https://gspe76-ssl.ls.apple.com/api/tile?"


def get_coverage_tile_raw(tile_x: int, tile_y: int, session: Session = None):
    headers = _build_coverage_tile_request_headers(tile_x, tile_y)
    requester = session if session else requests
    response = requester.get(COVERAGE_TILE_ENDPOINT, headers=headers)
    tile = MapTile_pb2.MapTile()
    tile.ParseFromString(response.content)
    return tile


async def get_coverage_tile_raw_async(tile_x: int, tile_y: int, session: ClientSession):
    headers = _build_coverage_tile_request_headers(tile_x, tile_y)

    async with session.get(COVERAGE_TILE_ENDPOINT, headers=headers) as response:
        content = await response.read()

    tile = MapTile_pb2.MapTile()
    tile.ParseFromString(content)
    return tile


def _build_coverage_tile_request_headers(tile_x, tile_y):
    headers = {
        "maps-tile-style": "style=57&size=2&scale=0&v=0&preflight=2",
        "maps-tile-x": str(tile_x),
        "maps-tile-y": str(tile_y),
        "maps-tile-z": "17",
        "maps-auth-token": "w31CPGRO/n7BsFPh8X7kZnFG0LDj9pAuR8nTtH3xhH8=",
    }
    return headers
