#!/usr/bin/python

from bs4 import BeautifulSoup
import rumps
import requests


class pokegostatus(rumps.App):

    @rumps.clicked("Manual refresh")
    def manual_refresh(self, _):
        self.refresh(self)

    @rumps.clicked("Black icons")
    def black_icons(self, _):
        self.refresh(self, "b")

    @rumps.clicked("White icons")
    def black_icons(self, _):
        self.refresh(self, "w")

    @rumps.timer(10)
    def refresh(self, _, icons="b"):
        URL = "http://cmmcd.com/PokemonGo/"

        try:
            r = requests.get(URL)
            soup = BeautifulSoup(r.text, 'html.parser')
            status = soup.body.header.h2.font.text
        except:
            status = False

        if status == 'Online!':
            self.icon = "icons/%s/pokeok.png" % icons
            self.title = None
        elif status == 'Unstable!':
            self.icon = "icons/%s/pokeunstable.png" % icons
            self.title = None
        elif status == 'Offline!':
            self.icon = "icons/%s/pokedown.png" % icons
            self.title = None
        elif not status:
            self.icon = None
            self.title = "No Internet"


if __name__ == "__main__":
    pokegostatus("pokegostatus", icon="icons/b/pokeinit.png").run()
