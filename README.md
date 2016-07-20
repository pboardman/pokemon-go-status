# Pokemon GO servers status

Check the status of the Pokemon GO servers from your Menubar (MacOS only)

![Demo](demo.png)

color code:

- green: server up
- orange: server unstable
- red: server down

To switch between black/white icons, use the menu items by clicking the icon.

## Installation

Just download `Pokemon.GO.Status.app.zip` from the [release page](https://github.com/Lacsap-/pokemon-go-status/releases/latest), unzip it, put it in your application folder and launch it!

Optionally you can launch it on startup start by going in your mac setting under `Users & Groups` and dragging the application in your `login items`.

## Making .app from source

- Install requirements

```pip install -r requirements.txt ```

- Build the .app

``` python setup.py py2app ```

note: Some peoples get errors when building the app with py2app,
if you do, try following the instruction in this
[link](http://stackoverflow.com/questions/25394320/py2app-modulegraph-missing-scan-code/29449144#29449144)

## Credit

The pokeball status icons were made by: [omgomg](https://github.com/omgmog)
