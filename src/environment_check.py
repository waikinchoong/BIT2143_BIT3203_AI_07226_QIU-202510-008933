"""Verify that the core AI laboratory packages are installed correctly."""

import matplotlib
import numpy
import pandas
import sklearn


def main() -> None:
    print("AI laboratory environment is ready.")
    print(f"NumPy: {numpy.__version__}")
    print(f"pandas: {pandas.__version__}")
    print(f"Matplotlib: {matplotlib.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")


if __name__ == "__main__":
    main()
