# Path Finder Robot Visualiser

A visualiser for a path finding bot that solves [this]([https://html-preview.github.io/?url=https://raw.githubusercontent.com/andrew1k3/dortmund/main/index.html](https://leetcode.com/problems/unique-paths-iii/description/)) leetcode question. 

## Description

This program brings a visualisation to the 'depth first search' algorithm and how it can be applied to trying to find a valid _path_ (a valid path is a path from start to finish that coverse _EVERY_ square).

## Preview

![movie2](https://github.com/andrew1k3/pathFinder/assets/95467716/b1986b58-d26e-4fa1-9925-0bff585dbbd9) ![movie](https://github.com/andrew1k3/pathFinder/assets/95467716/f71cacc7-fc09-45d1-b1de-09f12f91a5f6)

## Dependencies

- Python 3.0.0+
- MatPlotLib (`pip install matplotlib`)
- Glob (`pip install glob`)
- NumPy (`pip install numpy`)
- ImageIO (`pip install imageio`)

## How To Use

Go into /src/pathFinderBot.py and modify these variables at the bottom.
`grid` = Configure the grid for the bot to manuevere. (-1: Obstacle, 0: Nothing, 1: Robot, 2: Finish)
`render` = Enables rendering to the frames folder and tries to create a GIF of at movie.gif.
`print` = Enables printing to the console of recursive algorithm.
