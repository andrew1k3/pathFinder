# Path Finder Robot Visualiser

A visualiser for a path finding bot that solves [this](https://leetcode.com/problems/unique-paths-iii/description/) leetcode question. 

## Description

This program brings a visualisation to the 'depth first search' algorithm and how it can be applied to find all valid _pathes_.
- A valid path is a path from start to finish that coverse _EVERY_ square.

## Preview

![movie2-ezgif com-loop-count](https://github.com/andrew1k3/pathFinder/assets/95467716/7d97095e-82e2-4441-8f59-b222968d1daa)

## Dependencies

- Python 3.0.0+
- MatPlotLib `pip install matplotlib`
- Glob `pip install glob`
- NumPy `pip install numpy`
- ImageIO `pip install imageio`

## How To Use

Go into `/src/pathFinderBot.py` and modify these variables at the bottom.
- `grid` = Configure the grid for the bot to manuevere. (-1: Obstacle, 0: Nothing, 1: Robot, 2: Finish).
- `render` = Enables rendering to the frames folder and tries to create a GIF of at `movie.gif`.
- `print` = Enables printing to the console of recursive algorithm.
