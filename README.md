# reddit-research-tool
Business discussion analysis tool - Read-only Reddit API research platform
# Reddit Research Tool

Business discussion analysis tool for identifying relevant entrepreneurship and business discussions.

## Purpose

This tool helps small business owners and entrepreneurs discover valuable discussions across business-related subreddits. It performs read-only analysis to identify posts where business owners are seeking advice, sharing challenges, and discussing solutions.

## Features

- Search business-related subreddits for specific topics
- Analyze post content to identify genuine questions and discussions
- Categorize discussions by industry and problem type
- Read-only access - no posting, commenting, or voting

## Installation
```bash
pip install praw
```

## Configuration

Set environment variables:
```bash
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
```

## Usage
```python
python reddit_analyzer.py
```

## Targeted Subreddits

- r/entrepreneur
- r/smallbusiness
- r/startups
- r/sales
- r/marketing
- r/business

## License

MIT License - see LICENSE file
