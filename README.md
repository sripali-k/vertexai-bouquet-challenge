# 🌻 Google Cloud Skills Boost Challenge: Vertex AI - Bouquet Image Generator & Analyzer

This project was completed as part of a **Google Cloud Skills Boost** challenge. It focuses on using **Vertex AI's Imagen and Gemini models** to generate and analyze an image.

## 🚀 Challenge Overview

The challenge consisted of two main tasks:

---

## ✅ Task 1: Generate Bouquet Image

- **Objective**: Create a Python function that uses the `imagen-3.0-generate-002` model to generate an image of a bouquet.
- **Prompt Used**:  
  *"Create an image containing a bouquet of 2 sunflowers and 3 roses."*
- **Output**:  
  The generated image was saved locally as `image.jpeg`.

---

## ✅ Task 2: Analyze Bouquet Image

- **Objective**: Create a Python function that:
  - Takes the generated bouquet image as input
  - Sends it to the `gemini-2.0-flash-001` model with a text prompt to generate **birthday wishes**
  - Uses **streaming responses** or chat-based responses

- **Result**:  
  Gemini generated a beautiful birthday wish based on the bouquet image.

---

## 🛠 How I Ran the Code

✅ All code was run **inside the Google Cloud Skills Boost environment**, which:
- Automatically set up the project and region
- Provided access to Vertex AI services
- Required no manual API key or credentials setup

## 📂 Files

| File Name      | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| `genImage.py`  | Python script for Task 1: generating the bouquet image              |
| `genText.py`   | Python script for Task 2: analyzing the bouquet image with Gemini   |

---

## 🙌 Credits

This challenge and its resources were provided by the **[Google Cloud Skills Boost](https://www.cloudskillsboost.google/)** platform.

