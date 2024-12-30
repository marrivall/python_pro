import abc
from dataclasses import dataclass
import time
from typing import List

@dataclass
class SocialChannel(abc.ABC):
    type: str
    followers: int

    @abc.abstractmethod
    def post_a_message(self, message: str) -> None:
        pass

@dataclass
class Post:
    message: str
    timestamp: int

class YouTube(SocialChannel):
    def post_a_message(self, message: str) -> None:
        print(f"{message} to YouTube")

class Facebook(SocialChannel):
    def post_a_message(self, message: str):
        print(f"{message} to Facebook")

class Twitter(SocialChannel):
    def post_a_message(self, message: str):
        print(f"{message} to Twitter")

def process_schedule(posts: List[Post], channels: List[SocialChannel]) -> None:
    for post in posts:
        if post.timestamp <= time.time():
            for channel in channels:
                channel.post_a_message(post.message)

def main():
    posts = [Post(message="In the process of posting", timestamp=int(time.time()))]
    channels = [
        YouTube(type="YouTube", followers=764468),
        Facebook(type="Facebook", followers=2424),
        Twitter(type="Twitter", followers=1234),
    ]
    process_schedule(posts, channels)

if __name__ == "__main__":
    main()



# # each social channel has a type and the current number of followers
# SocialChannel = tuple[str, int] --- class

# def post_a_message(channel: SocialChannel, message: str) ---  abstraction in SocialChannel
# "youtube", "facebook", "twitter" ---classes to every chanel

# # each post has a message and the timestamp when it should be posted
# Post = tuple[str, int] --- class

# def process_schedule(posts: list[Post], channels: list[SocialChannel]) -> None:
#     for post in posts:
#         message, timestamp = post
#         for channel in channels:
#             if timestamp <= time():
#                 post_a_message(channel, message)

#timestamp - indicates the date and time at which a particular event has occurred