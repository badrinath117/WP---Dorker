import os
import sys
import requests
from googlesearch import search

def search_and_check_results(query):
    search_query = query + " site:example.com"
    search_results = list(search(search_query, num=1, stop=1, pause=2))

    if search_results:
        print(f"Results found for query '{query}':")
        for result in search_results:
            print(result)
        print()
    else:
        print(f"No results found for query '{query}'.")

if len(sys.argv) != 2:
    print("Usage: python google_search_checker.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

if not os.path.exists(filename):
    print(f"File '{filename}' not found.")
    sys.exit(1)

with open(filename, 'r') as file:
    for line in file:
        query = line.strip()
        if query:
            search_and_check_results(query)
