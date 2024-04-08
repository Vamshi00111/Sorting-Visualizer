import sys
from typing import List
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BAR_WIDTH = 5
GAP = 2
NUM_BARS = SCREEN_WIDTH // (BAR_WIDTH + GAP)
BAR_HEIGHT_MAX = SCREEN_HEIGHT - 50
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sorting Visualizer")

# Generate random list of heights for bars
bar_heights = [random.randint(1, BAR_HEIGHT_MAX) for _ in range(NUM_BARS)]

# Bubble Sort algorithm
def bubbleSort(nums):
    n = len(nums)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if nums[j+1] < nums[j]: 
                nums[j+1], nums[j] = nums[j], nums[j+1]
                swapped = True
                # Refresh the screen after every swap
                draw(nums)
                pygame.time.delay(10)
        if swapped == False: break #will break the loop if the array is already sorted, Making the code more efficient
        #This works because you check the every adjacent pair

# Function to draw the bars
def draw(arr):
    screen.fill(WHITE)
    for i, height in enumerate(arr):
        pygame.draw.rect(screen, BLUE, (i*(BAR_WIDTH+GAP), SCREEN_HEIGHT-height, BAR_WIDTH, height))
    pygame.display.update()

# Main function
def main():
    running = True
    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        bubbleSort(bar_heights)
        draw(bar_heights)

    pygame.quit()

if __name__ == "__main__":
    main()
