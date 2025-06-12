#!/usr/bin/python3
import requests
import csv

def fetch_and_print_posts():
    """Fetch posts and print titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """Fetch posts and save to CSV"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        filtered_posts = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]

        with open("posts.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)
