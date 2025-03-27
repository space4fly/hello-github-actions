import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"
from kivy.app import App
from kivy.uix.videoplayer import VideoPlayer
from kivy.uix.boxlayout import BoxLayout

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
}


class VideoApp(App):
    def __init__(self, source, **kwargs):
        super().__init__(**kwargs)
        self.source = source  # 保存传入的视频源参数

    def build(self):
        layout = BoxLayout()
        # 使用实例变量中的source参数
        video_player = VideoPlayer(source=self.source)
        layout.add_widget(video_player)
        video_player.state = 'play'
        return layout

if __name__ == '__main__':
    # 通过参数传递视频源（这里以示例URL演示）
    video_url = 'http://223.110.243.172/PLTV/3/224/3221227207/index.m3u8'
    VideoApp(source=video_url).run()
