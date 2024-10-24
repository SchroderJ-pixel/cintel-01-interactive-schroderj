import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

with ui.sidebar():
    ui.input_slider("n", "Number of Bins", 1, 50, 31)

# Title of the project
@render.text()
def title():
    text = "P1: Interactive App: Slider Input & Histogram Output"
    title_text = text.title()
    return title_text

@render.plot(alt="A histogram")
def histogram():
    np.random.seed(19680801)
    x = 100 + 15 * np.random.randn(437)
    
    # Calculate histogram
    counts, bin_edges = np.histogram(x, bins=input.n(), density=False)
    norm_counts = counts / np.max(counts)

    # Rainbow colormap
    colors = plt.cm.rainbow(norm_counts)
    plt.bar(bin_edges[:-1], counts, width=np.diff(bin_edges), color=colors, edgecolor='black')

    # Mean, median, and standard deviation
    mean_val = np.mean(x)
    median_val = np.median(x)
    std_val = np.std(x)

    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='green', linestyle='dashed', linewidth=1, label=f'Median: {median_val:.2f}')
    plt.axvline(mean_val + std_val, color='purple', linestyle='dashed', linewidth=1, label=f'Std Dev: {std_val:.2f}')
    plt.axvline(mean_val - std_val, color='purple', linestyle='dashed', linewidth=1)

    # Labels and title
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title("Histogram with Frequency-Based Colors and Statistics")
    
    plt.legend()


