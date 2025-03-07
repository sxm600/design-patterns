from abc import ABC, abstractmethod


class ThirdPartyYoutubeLib(ABC):
    @abstractmethod
    def list_videos(self): ...

    @abstractmethod
    def get_video_info(self, id): ...

    @abstractmethod
    def download_video(self, id): ...


class ThirdPartyYoutubeClass(ThirdPartyYoutubeLib):
    def list_videos(self): ...

    def get_video_info(self, id): ...

    def download_video(self, id): ...


class CachedYoutubeClass(ThirdPartyYoutubeLib):
    def __init__(self, service: ThirdPartyYoutubeLib):
        self.service = service
        self.list_cache = None
        self.video_cache = None
        self.needs_reset = False


    def list_videos(self):
        if self.list_cache is None or self.needs_reset:
            self.list_cache = self.service.list_videos()

        return self.list_cache

    def get_video_info(self, id):
        if self.video_cache is None or self.needs_reset:
            self.video_cache = self.service.get_video_info(id)

        return self.video_cache

    def download_video(self, id):
        if self.needs_reset:
            self.service.download_video(id)


class YoutubeManager:
    def __init__(self, service: ThirdPartyYoutubeLib):
        self.service = service

    def render_video_page(self, id):
        info = self.service.get_video_info(id)
        ...

    def render_list_panel(self):
        videos = self.service.list_videos()
        ...

    def react_on_user_input(self, id):
        self.render_video_page(id)
        self.render_list_panel()


def main():
    service = ThirdPartyYoutubeClass()
    proxy = CachedYoutubeClass(service)
    manager = YoutubeManager(proxy)
    manager.react_on_user_input(1)
