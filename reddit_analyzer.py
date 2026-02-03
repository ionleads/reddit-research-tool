# reddit_analyzer.py
import praw
import os

# Initialize Reddit API
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent='ION Research Tool/1.0'
)

# Search for business discussions
def search_business_discussions(keyword, subreddit_name, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    results = []
    
    for post in subreddit.search(keyword, limit=limit, time_filter='month'):
        results.append({
            'title': post.title,
            'author': str(post.author),
            'created': post.created_utc,
            'score': post.score,
            'url': post.url
        })
    
    return results

# Example: Find posts about client acquisition
if __name__ == '__main__':
    discussions = search_business_discussions(
        keyword='finding clients',
        subreddit_name='entrepreneur',
        limit=50
    )
    
    for d in discussions:
        print(f"{d['title']} - {d['score']} upvotes")
```
