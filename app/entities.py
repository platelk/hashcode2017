"""
List entities returned by the parsing
"""


class InputData:
    def __init__(self, videos, endpoints, requests, cache_servers):
        self.videos = videos
        self.endpoints = endpoints
        self.cache_servers = cache_servers
        self.requests = requests


class Video:
    def __init__(self, size=0):
        self.size = size


class Endpoint:
    def __init__(self, latency=0):
        # Latency to datacenter
        self.latency = latency
        # List of maps
        self.cache_servers = []
        self.requests = []


class CacheServer:
    def __init__(self, server_id=0, max_size=0):
        self.id = server_id
        self.available_size = max_size
        self.videos = []
        self.max_size = max_size

    def add_video(video):
        self.videos.append(video)
        self.available_size -= video.size


class Request:
    def __init__(self, video_id, origin_endpoint, requests_sum):
        self.video_id = video_id
        self.origin_endpoint = origin_endpoint
        self.requests_sum = requests_sum
