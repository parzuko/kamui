# Kamui 
Get the shortest path between two metro stations!
> Complete list of supported stations [here](https://github.com/parzuko/kamui/blob/main/assets/station_list.txt)

## :thinking: How It Works?
You can add `Kamui` to your discord server using [this link](https://discord.com/api/oauth2/authorize?client_id=969337544221270106&permissions=156766816320&scope=bot%20applications.commands)

![kamui](https://user-images.githubusercontent.com/57803819/166148661-2a8a3de9-69d0-483c-9836-0dbe26fca368.gif)


Kamui is based on Dijkstra's algorithm.

The logic for this is in `MetroGraph` class inside `models.py`. The time between stations is used as the weight as between nodes(stations)

## :computer: Installing Locally

```bash

# Clone this repository.
git clone https://github.com/parzuko/kamui.git
cd kamui

# Setup Your Personal Tokens
echo >> "BOT_TOKEN=<YOUR_TOKEN>" >> .env

# Install pipenv
pip install pipenv

# Install dependencies
pipenv install pipfile

# Run it locally
pipenv shell
python3 main.py

```

---

Made for Intro to Computer Programming Spring 2022 (And For Fun!) :v: [Say Hi!](https://twitter.com/parzuko)
