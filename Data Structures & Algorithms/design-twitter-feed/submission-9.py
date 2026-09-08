class Twitter:

    def __init__(self):
        self.following = defaultdict(set) # user -> following
        self.posts = defaultdict(list) # user -> posts
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        heap = []
        for user in self.following[userId]:
            num_posts = len(self.posts[user])
            # (-time, tweetId, user, index)
            if self.posts[user]: # if they have posts, add most recent
                t, tid = self.posts[user][-1]
                heapq.heappush(heap, (-t, tid, user, num_posts-1))
        if self.posts[userId]:
            t, tid = self.posts[userId][-1]
            heapq.heappush(heap, (-t, tid, userId, len(self.posts[userId])-1))

        for i in range(10):
            if not heap:
                return feed
            neg_t, tid, user, index = heapq.heappop(heap)
            feed.append(tid)
            if index != 0:
                prev_t, prev_tid = self.posts[user][index-1]
                heapq.heappush(heap, (-prev_t, prev_tid, user, index-1))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)