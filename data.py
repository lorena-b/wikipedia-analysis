"""
File for scraping wikipedia data to locate the links to Kevin Bacon
Copyright
"""
import requests
import csv
from bs4 import BeautifulSoup

GOAL = 'Kevin Bacon'
LIMIT = 50  # change according to runtime


def get_direct_links_csv(goal: str, limit: int) -> None:
    """Find all the articles that directly link to the goal article
    """
    response = requests.get(
        # Use the backlinks route
        url='https://en.wikipedia.org/w/index.php?title=Special%3AWhatLinksHere&' +
            'limit=' + str(limit) + '&target=' + goal + '&namespace='
    )
    print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find(id='bodyContent').find_all('a')

    with open('links.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        for link in links:

            is_special = 'Special' in str(link)
            is_wiki = '/wiki/' in str(link)
            is_goal_article = goal in str(link)

            if is_wiki and not is_goal_article and not is_special:
                writer.writerow(link)
                print(link)


def get_direct_links(goal: str, limit: int) -> list:
    """Find all the articles that directly link to the goal article
    """
    response = requests.get(
        # Use the backlinks route
        url='https://en.wikipedia.org/w/index.php?title=Special%3AWhatLinksHere&' +
            'limit=' + str(limit) + '&target=' + goal + '&namespace='
    )
    print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find(id='bodyContent').find_all('a')

    data = []

    for link in links:

        is_special = 'Special' in str(link)
        is_wiki = '/wiki/' in str(link)
        is_goal_article = goal in str(link)

        if is_wiki and not is_goal_article and not is_special:
            data.append(link)

    return data


if __name__ == "__main__":
    get_direct_links(GOAL, LIMIT)
