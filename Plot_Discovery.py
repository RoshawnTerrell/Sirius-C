import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits

def plot_evidence():
    print("Generating Evidence Graph...")

    # --- INPUT FILES (Check these match your folder) ---
    file_sirius = "Gravity_Raw.fits"       # The file with ~23 deg Phase
    file_control = "Control_Star_Raw.fits" # The file with ~0.6 deg Phase

    plt.figure(figsize=(10, 6))

    # 1. Plot Control (Blue/Stable)
    try:
        with fits.open(file_control) as hdul:
            data = hdul['OI_T3'].data['T3PHI']
            plt.plot(data, color='blue', alpha=0.6, label='Control Star (Omicron Pup)', linewidth=1.5)
            print(" > Plotted Control Star")
    except:
        print(" ! Could not find Control file")

    # 2. Plot Sirius A (Red/Perturbed)
    try:
        with fits.open(file_sirius) as hdul:
            data = hdul['OI_T3'].data['T3PHI']
            plt.plot(data, color='red', alpha=0.8, label='Sirius A (Target)', linewidth=1.5)
            print(" > Plotted Sirius A")
    except:
        print(" ! Could not find Sirius file")

    # 3. Formatting
    plt.axhline(0, color='black', linestyle='--')
    plt.title("DETECTION OF COMPANION: SIRIUS A vs CONTROL", fontsize=14, fontweight='bold')
    plt.xlabel("Spectral Channel", fontsize=12)
    plt.ylabel("Closure Phase (Degrees)", fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Save
    plt.savefig("Sirius_Discovery_Graph.png", dpi=300)
    print("SUCCESS: Graph saved as 'Sirius_Discovery_Graph.png'")
    plt.show()

if __name__ == "__main__":
    plot_evidence()