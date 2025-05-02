🌸 Bouquet Image Generator & Analyzer
This project was developed as part of a cloud-based AI challenge on Qwiklabs. It demonstrates how to generate an image using the Vertex AI Imagen model and analyze that image using the Gemini multimodal model.

🚀 Tasks
Task 1: Generate Bouquet Image
Function: generate_bouquet_image()

Purpose: Generates an image of a bouquet with 2 sunflowers and 3 roses using the imagen-3.0-generate-002 model.

Output: Saves the generated image locally as bouquet_image.jpeg.

Task 2: Analyze Bouquet Image
Function: analyze_bouquet_image(image_path)

Purpose: Sends the generated image to the gemini-2.0-flash-001 model to create a birthday wish based on the image.

Key Feature: Uses streaming to fetch content as it’s generated.

🛠️ How to Run
Install dependencies:

nginx
Copy
Edit
pip install google-cloud-aiplatform vertexai
Run the script:

bash
Copy
Edit
/usr/bin/python3 genImage.py
/usr/bin/python3 genText.py
📂 Files
genImage.py – Contains the code to generate the bouquet image.

genText.py – Contains the code to analyze the bouquet image and stream the generated birthday wish.

README.md – Project description and instructions.

✅ Notes
Ensure that Vertex AI is initialized with the correct project ID and region.

The image should be saved as bouquet_image.jpeg (or image.jpeg if specified).

The Gemini model response is streamed and displayed in the terminal.