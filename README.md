# SVM_Tutorial

A tutorial on support vector machines created for the COP506 module at Loughborough University.

The tutorial provides an introduction to Support Vector Machines (SVMs), a supervised learning algorithm used for classification tasks. Using a real-world example, it explains the mathematical principles behind SVMs and guides readers through a practical implementation using the scikit-learn library.

There are three ways to view the tutorial:

## A: Online via Binder

Click the following button to view and interact with the tutorial online: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/VincentVoigtlaender/SVM_Tutorial/HEAD?urlpath=%2Fdoc%2Ftree%2Fsvm_tutorial.ipynb)

## B: Offline as Jupyter Notebook

Alternatively, you can clone or download the repository, to run the notebook locally.

The tutorial is written for `Python 3.12`, which must be available on your machine.

The required packages can be installed into a virtual environment via
```bash
cd <folder containing this README.md>
python3 -m venv .venv
pip install -r requirements.txt
```

Finally, you can start Jupyter Lab to open and interact with the tutorial
```bash
jupyter lab svm_tutorial.ipynb
```

## C: Offline as .html (non-interactive)

If you do not wish to use the interactive elements but only want to read the tutorial, you can also view the exported [.html file](./svm_tutorial.html) using any web browser.
