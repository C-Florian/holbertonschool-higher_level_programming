#!/usr/bin/env python3
"""
Task 02 - Fetch and process data from JSONPlaceholder API
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.
    Also prints the HTTP response status code.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # Print the HTTP status code
    print(f"Status Code: {response.status_code}")

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON data
        posts = response.json()

        # Print the title of each post
        for post in posts:
            print(post['title'])
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetch all posts and save them to a CSV file (id, title, body).
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Extract relevant fields into a list of dictionaries
        data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Write the data to a CSV file
        with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)
        print("Posts successfully saved to posts.csv")
    else:
        print("Failed to fetch posts.")

