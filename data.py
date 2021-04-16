"""CSC111 Winter 2021 Final Project: Data Collection

This file contains functions for scraping wikipedia to obtain data.

This file is Copyright (c) 2021 Lorena Buciu, Luke Kuo, Aidan Ryan, Kevin Yang
"""
import csv
import requests
from bs4 import BeautifulSoup


def get_direct_links_csv(goal: str, limit: int) -> None:
    """Find all the articles that directly link to the goal article.

    Preconditions:
        - limit > 0
    """
    response = requests.get(
        # Use the backlinks route
        url='https://en.wikipedia.org/w/index.php?title=Special%3AWhatLinksHere&' + 'limit='
        + str(limit) + '&target=' + goal + '&namespace='
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


def get_direct_links(goal: str, limit: int) -> list:
    """Find all the articles that directly link to the goal article.

    Preconditions:
        - limit > 0
    """
    response = requests.get(
        # Use the backlinks route
        url='https://en.wikipedia.org/w/index.php?title=Special%3AWhatLinksHere&' + 'limit='
        + str(limit) + '&target=' + goal + '&namespace='
    )
    # print(response.status_code)

    soup = BeautifulSoup(response.content, 'html.parser')
    links = soup.find(id='bodyContent').find_all('a')

    data = []

    for link in links:

        is_special = 'Special' in str(link)
        is_wiki = '/wiki/' in str(link)
        is_goal_article = goal in str(link)

        if is_wiki and not is_goal_article and not is_special:
            data.append(link.text)

    return data


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'max-nested-blocks': 4,
        'disable': ['E1136', 'E9998'],
        'extra-imports': ['csv', 'requests', 'bs4'],
        'allowed-io': []
    })
