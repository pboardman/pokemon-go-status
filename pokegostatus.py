#!/usr/bin/python

from bs4 import BeautifulSoup
import rumps
import requests
import os


class pokegostatus(rumps.App):

    icons = ""
    config_file = "{0}/.pokecheck".format(os.path.expanduser("~"))
    if not os.path.isfile(config_file):
        with open(config_file, "w") as f:
            f.write("black\n")
        icons = "b"
    else:
        with open(config_file, "r") as f:
            content = f.read()
            if "black" in content:
                icons = "b"
            elif "white" in content:
                icons = "w"


    @rumps.clicked("Manual refresh")
    def manual_refresh(self, _):
        self.refresh(self)

    @rumps.clicked("Black icons")
    def black_icons(self, _):
        with open(self.config_file, "w") as f:
            f.write("black\n")
            self.icons = "b"
        self.refresh(self)

    @rumps.clicked("White icons")
    def black_icons(self, _):
        with open(self.config_file, "w") as f:
            f.write("white\n")
            self.icons = "w"
        self.refresh(self)

    @rumps.timer(10)
    def refresh(self, _):
        URL = "http://cmmcd.com/PokemonGo/"

        try:
            r = requests.get(URL)
            soup = BeautifulSoup(r.text, 'html.parser')
            status = soup.body.header.h2.font.text
        except:
            status = False

        if status == 'Online!':
            self.icon = "icons/%s/pokeok.png" % self.icons
            self.title = None
        elif status == 'Unstable!':
            self.icon = "icons/%s/pokeunstable.png" % self.icons
            self.title = None
        elif status == 'Offline!':
            self.icon = "icons/%s/pokedown.png" % self.icons
            self.title = None
        elif not status:
            self.icon = None
            self.title = "No Internet"


if __name__ == "__main__":
    pokegostatus("pokegostatus", icon="icons/b/pokeinit.png").run()
