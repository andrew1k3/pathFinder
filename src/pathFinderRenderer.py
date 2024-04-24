import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from typing import List
import copy
import os
import imageio
import glob

plt.rcParams["font.family"] = "monospace"

class Solution:
    def __init__(self, print, render):
        self.counter = 0
        self.frameNumber = 0
        self.print = print
        self.render = render

        self.colours = dict(
            PATH = '#6096ba',
            FLAG = '#79fc5b',
            ROBOT = '#274c77',
            OBSTACLE = '#f52a2a',
        )

    def counter_up(self):
        self.counter += 1
    
    def frame_up(self):
        self.frameNumber += 1

    def renderFrame(self, grid, current, seen, entering, escaping, finish, found, foundTooEarly):
        if (not self.render): return
        counter = copy.deepcopy(self.counter)
        grid = copy.deepcopy(grid)
        seen = copy.deepcopy(seen)
        grid[current] = 1
        for x in seen:
            grid[x] = 3

        # Prepare frame
        fig, ax = plt.subplots()
        cmap = colors.ListedColormap([self.colours["OBSTACLE"], "black", self.colours["ROBOT"], self.colours["FLAG"], self.colours["PATH"]])
        bounds = [-1,0,1,2,3,4]
        norm = colors.BoundaryNorm(bounds, cmap.N)
        img = ax.imshow(grid, cmap=cmap, norm=norm)
        for i in range(grid.shape[0]):
            ax.axhline(0.5 + i, color='white')
        for i in range(grid.shape[1]):
            ax.axvline(0.5 + i, color='white')
        ax.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False, length=0)
        ax.set_yticks(range(grid.shape[0])) 
        ax.set_xticks(range(grid.shape[1])) 

        X_WEST = 1.05
        Y_TOP = 1.00
        Y_SHIFT = 0.06
        ylabelpos = lambda n : Y_TOP - n * Y_SHIFT

        # If list is too long to fit in frame (weird solution)
        if (len(seen) > 16): 
            seen = seen[len(seen)-16:]
            seen.insert(0, "...")

        # Render text
        ax.text(0, 1.1, f'Seen: {seen}', transform=ax.transAxes, fontsize="5")
        ax.text(X_WEST, ylabelpos(1), f'Current: {current}', transform=ax.transAxes)
        ax.text(X_WEST, ylabelpos(2), f'Entering', transform=ax.transAxes, color='g' if entering else 'r')
        ax.text(X_WEST, ylabelpos(3), f'Escaping', transform=ax.transAxes, color='g' if escaping else 'r')
        ax.text(X_WEST, ylabelpos(4), f'Finishing', transform=ax.transAxes, color='g' if finish else 'r')
        ax.text(X_WEST, 0.10, f'Total Paths Found: {counter}', transform=ax.transAxes, fontsize="20")

        if found:
            ax.text(X_WEST, 0.50, f' :)', transform=ax.transAxes, fontsize="25", color='g')
        if foundTooEarly:
            ax.text(X_WEST, 0.50, f'>:(', transform=ax.transAxes, fontsize="25", color='r')
            
        filetag = "./src/frames/"
        fig.savefig(f"{filetag}{str(self.frameNumber).zfill(6)}.png", bbox_inches="tight")
        self.frame_up()

        plt.close()

    def renderGif(self) -> None:
        if (not self.render): return
        if self.print: print(f"Generating GIF with {self.frameNumber} frames")
        images = []
        for filename in sorted(glob.glob('./src/frames/*')):
            images.append(imageio.imread(filename))
        try:
            imageio.mimsave('./src/movie.gif', images, format='GIF', fps=120, loop=0)
        except Exception as e:
            print("Gif failed", e)

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        grid = np.array(grid)
        numZeros = sum((grid == 0).flatten()) # ARE YOU HAPPY JAMES ARE YOU HAPPY ARE YOU HAPPY
        start = (lambda x: (x[0][0], x[1][0]))(np.where(grid == 1))

        # Recursive Depth First Search to find paths. If path found, add one to self.counter.
        def dfs(current, seen) -> None:
            if grid[current] == 2:
                if self.print: print("IM AT FINISH")
                self.renderFrame(grid, current, seen, False, True, True, False, False)
                if len(seen) == numZeros + 1:
                    if self.print: print('great success')
                    self.counter_up()
                    self.renderFrame(grid, current, seen, False, True, True, True, False)
                    return
                else:
                    if self.print: print('at end too early')
                    self.renderFrame(grid, current, seen, False, True, True, False, True)
                    return
                
            seen = copy.deepcopy(seen)
            seen.append(current)
        
            def next_is_valid(new) -> bool:
                return (
                    0 <= new[0] < grid.shape[0] # in the grid
                    and 0 <= new[1] < grid.shape[1]
                    and grid[new] != -1 # not an obstacle
                    and new not in seen # not visited before
                )

            # top
            new = (current[0] - 1, current[1])
            if next_is_valid(new):
                if self.print: print(len(seen)*'>', 'entered ↑')
                self.renderFrame(grid, current, seen[:-1], True, False, False, False, False)
                dfs(new, seen)
                if self.print: print(len(seen)*'<', 'escaped ↓ ')
            
            # down
            new = (current[0] + 1, current[1])
            if next_is_valid(new):
                if self.print: print(len(seen)*'>', 'entered ↓ ')
                self.renderFrame(grid, current, seen[:-1], True, False, False, False, False)
                dfs(new, seen)
                if self.print: print(len(seen)*'<', 'escaped ↑')

            # west
            new = (current[0], current[1] - 1)
            if next_is_valid(new):
                if self.print: print(len(seen)*'>', 'entered ←')
                self.renderFrame(grid, current, seen[:-1], True, False, False, False, False)
                dfs(new, seen)
                if self.print: print(len(seen)*'<', 'escaped →')

            # starboard
            new = (current[0], current[1] + 1)
            if next_is_valid(new):
                if self.print: print(len(seen)*'>', 'entered →')
                self.renderFrame(grid, current, seen[:-1], True, False, False, False, False)
                dfs(new, seen)
                if self.print: print(len(seen)*'<', 'escaped ←')

            self.renderFrame(grid, current, seen[:-1], False, True, grid[current] == 2, False, False)

        if self.render:
            if self.print: print("Deleting old frames")
            for file in glob.glob('./src/frames/*'):
                os.remove(file)

        dfs(start, [])
        self.renderGif()

        return self.counter

# TEST CASES

# grid = [
#     [1,0,0,0],
#     [0,0,-1,0],
#     [0,0,0,0],
#     [0,0,2,-1]]

# grid = [[1,0,0,-1,2],
#         [0,0,0,-1,0],
#         [-1,-1,0,0,0],]

# grid = [
#     [ 1, 0, 0, 0],
#     [-1,-1,-1, 0],
#     [ 0, 0, 0, 0],
#     [ 0, 0, 0,-1],
#     [ 0, 0, 2,-1]]

grid = [[ 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1,-1, 0, 0,-1,-1,-1,-1, 0],
        [ 2, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1,-1, 0, 0,-1,-1,-1,-1,-1]]

solution = Solution(print=True, render=True)
answer = solution.uniquePathsIII(grid)
if solution.print: print(answer)
