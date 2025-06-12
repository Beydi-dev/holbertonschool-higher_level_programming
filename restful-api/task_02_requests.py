def fetch_and_save_posts(url):
    response = requests.get(url)
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        filtered_posts = []

        for post in posts:
            filtered_posts.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        import csv
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(filtered_posts)
