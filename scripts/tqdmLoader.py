# from tqdm import *
# from time import sleep

# for i in tqdm(range(10)):
#     sleep(0.5)
from tqdm import tqdm
import time

# Define the colors that you want to use for the progress bar
colors = ['blue', 'green', 'red']

# Create a progress bar
pbar = tqdm(total=100)

# Iterate over the progress bar and update the color
for i in range(100):
    time.sleep(0.2)
    pbar.update(1)
    pbar.set_description(f"{colors[i % len(colors)]}{i}%")

# Close the progress bar
pbar.close()