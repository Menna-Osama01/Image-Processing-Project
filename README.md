# 🎨 Fixel – Image Enhancement Web App

[![Python](https://img.shields.io/badge/python-3.11-blue.svg?style=flat-square)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-orange.svg?style=flat-square)](https://streamlit.io/)  
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](LICENSE)

**Fixel** is a web application for image enhancement and transformation. Users can upload or capture images and apply various digital image processing techniques, including **Thresholding**, **Power-Law (Gamma) Transformation**, **Linear Negative Transformation**, and **Morphological Operations**.

---

## 📝 Overview

Fixel is designed to demonstrate practical applications of **image processing techniques** in an interactive way. With a few clicks, users can:

- Enhance images for better visualization
- Apply different transformations for analysis or aesthetic purposes
- Download the enhanced images

---

## 💻 Features

### Image Enhancement Techniques
1. **Thresholding** – Useful for segmentation, object detection, OCR preprocessing, and edge detection.  
2. **Linear Negative Transformation** – Inverts grayscale images for highlighting dark regions, medical imaging, or photographic negatives.  
3. **Power-Law (Gamma) Transformation** – Nonlinear adjustment of pixel values to control brightness and contrast.  
4. **Morphological Transformation** – Shape-based operations (Erosion, Dilation, Opening, Closing) for noise removal, hole filling, and edge detection.

### User-Friendly Interface
- Upload images (`.jpg`, `.png`, `.jpeg`) or capture with camera
- Select enhancement technique and adjust parameters using sliders
- Compare original and enhanced images side by side
- Download the enhanced image as PNG

---

## 🖼 Screenshots

*(Optional: Add screenshots here if you have them, e.g., original vs enhanced images)*  

![Fixel Demo](ImageProject/finallogo.png)  

---

## 🔧 Installation & Running

1. Clone the repository:

```bash

2. Install dependencies:
pip install streamlit numpy opencv-python pillow

3. Run the web app:
streamlit run ML.ipynb
git clone <repository-url>
cd <repository-folder>
