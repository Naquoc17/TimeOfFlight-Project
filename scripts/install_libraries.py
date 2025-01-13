import subprocess
import sys

def install_libraries():
    """
    Function to install required libraries using pip.
    Libraries to be installed: scipy.ndimage, numpy, PIL
    """
    # List of required libraries
    libraries = [
        "scipy",
        "numpy",
        "Pillow",  # PIL is now part of Pillow package
        "opencv-python",
        "ultralytics",
    ]

    for library in libraries:
        try:
            # Attempt to install the library
            print(f"Installing {library}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library, "--no-warn-script-location"])
            print(f"{library} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"Failed to install {library}. Please check your environment and try again.")

if __name__ == "__main__":
    install_libraries()
