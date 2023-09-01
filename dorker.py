import os
import sys
import time
import requests
from googlesearch import search

# Function to perform a Google search and check if there are results
def search_and_check_results(query, site_param):
    search_query = query + f" site:{site_param}"
    
    # Add a custom User-Agent header to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    
    try:
        search_results_dict = search(search_query, num=10, stop=10, pause=2, user_agent=headers)
        
        # Limit the number of results to 1
        search_results_dict = search_results_dict[:1]
        
        # Extract search results from the dictionary
        search_results = [result['link'] for result in search_results_dict]
        
        if search_results:
            print(f"Results found for query '{query}':")
            for result in search_results:
                print(result)
            print()
        else:
            print(f"No results found for query '{query}'.")
    except Exception as e:
        print(f"Error occurred for query '{query}': {str(e)}")

# Check if two command-line arguments are provided
if len(sys.argv) != 3:
    print("Usage: python google_search_checker.py <filename> <site_param>")
    sys.exit(1)

filename = sys.argv[1]
site_param = sys.argv[2]

# Check if the file exists
if not os.path.exists(filename):
    print(f"File '{filename}' not found.")
    sys.exit(1)

# Read and process each line in the file
with open(filename, 'r') as file:
    for line in file:
        query = line.strip()
        if query:
            search_and_check_results(query, site_param)
            # Add a delay between requests to avoid rate limiting
            time.sleep(5)  # Adjust this delay as needed
