# Astro

An "oraCLI" for determining the astrological sign associated with a POSIX timestamp. Optional support for Ophiucus reluctantly forthcoming.

# Use cases

Get the astrological sign for your vm or tmux session or a long-running process.

Check on your production servers and restart any host that's a pisces or a cancer (very temperamental).

Maybe kick off a cron to do sentiment analysis on your favorite horoscopes and register a nagios alert to catch any doom-and-gloom predictions for relevant signs.

You're welcome.

# Installation

Get [pipsi](https://github.com/mitsuhiko/pipsi#readme)! Clone this repo, cd in and just:

    $ pipsi install .

# Usage

    $ astro [timestamp]

or

    $ echo [timestamp] | astro

# Thanks

Created with [CookieCutter](https://github.com/nvie/cookiecutter-python-cli).
