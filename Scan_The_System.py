import os
import glob
import numpy as np
from astropy.io import fits

def scan_system():
    print("\n--- SIRIUS C DETECTOR & CONTROL CHECK ---")
    print(f"{'FILENAME':<35} | {'TARGET':<15} | {'PHASE (Wobble)':<15} | {'VERDICT'}")
    print("-" * 85)
    
    files = glob.glob("*.fits")
    
    for f in files:
        try:
            with fits.open(f) as hdul:
                # 1. Get Target Name
                header = hdul[0].header
                target = header.get('OBJECT', 'Unknown')
                
                # 2. Get Phase (The "Wobble")
                if 'OI_T3' in hdul:
                    t3 = hdul['OI_T3'].data['T3PHI']
                    phase = np.mean(t3)
                else:
                    phase = 0.0

                # 3. Get Visibility (The "Size")
                # Vis < 0.1 = Giant Star (Sirius A)
                # Vis > 0.5 = Point Source (Control)
                if 'OI_VIS2' in hdul:
                    vis = np.mean(hdul['OI_VIS2'].data['VIS2DATA'])
                else:
                    vis = 0.0

                # --- THE LOGIC ---
                if abs(phase) > 10.0 and vis < 0.2:
                    verdict = ">>> ANOMALY (Sirius A + C)"
                elif abs(phase) < 2.0 and vis > 0.5:
                    verdict = "VALID CONTROL (Stable)"
                elif abs(phase) < 2.0 and vis < 0.2:
                    verdict = "Sirius A (Stabilizer Data)"
                else:
                    verdict = "Unclear"

                print(f"{f[:35]:<35} | {target[:15]:<15} | {phase:>8.2f} deg    | {verdict}")

        except Exception as e:
            pass 

    print("-" * 85)

if __name__ == "__main__":
    scan_system()