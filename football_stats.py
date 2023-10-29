import requests
from bs4 import BeautifulSoup

def get_top_20_players():
    # URL to the CBS NFL Stats webpage
    url = "http://www.cbssports.com/nfl/stats"
    
    # Make a request to the webpage
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Parse the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract the top 20 players based on the provided tags
    players = soup.find_all('div', class_='StatsLeadersCard-featuredStat', limit=20)
    
    for player in players:
        touchdowns = player.find('div', class_='StatsLeadersCard-statValue').text.strip()
        stat_title = player.find('div', class_='StatsLeadersCard-statTitle').text.strip()
        
        # Assuming there are other tags for player's name, position, and team, you can extract them similarly
        # For this example, I'll only print the touchdowns and stat title
        print(f"{stat_title}: {touchdowns}")

if __name__ == "__main__":
    get_top_20_players()