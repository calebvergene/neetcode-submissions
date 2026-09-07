class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # user -> following
        self.posts = defaultdict(list) # user -> posts
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        for user in self.following[userId]:
            num_posts = len(self.posts[user])
            # (postId, userId, index)
            if self.posts[user]: # if they have posts, add most recent
                heapq.heappush(heap, (-self.posts[user][-1], user, num_posts-1))
        if self.posts[userId]:
            heapq.heappush(heap, (-self.posts[userId][-1], userId, len(self.posts[userId])-1))

        for i in range(10):
            if not heap:
                return feed
            post, user, index = heapq.heappop(heap)
            feed.append(-post)
            if index != 0:
                heapq.heappush(heap, (-self.posts[user][index-1], user, index-1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].remove(followeeId)
