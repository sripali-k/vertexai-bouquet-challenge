# Bouquet Image Generation and Analysis Challenge

## Description

This repository contains a Python project that demonstrates the use of **Vertex AI** models to:

1. **Generate an image** of a bouquet based on a given prompt.
2. **Analyze the generated image** using a multimodal model to generate birthday wishes.

### Task Breakdown:

- **Task 1**: Generates an image using the **Imagen** model based on a prompt: _"Create an image containing a bouquet of 2 sunflowers and 3 roses."_ The generated image is saved locally.
  
- **Task 2**: Analyzes the saved image using the **Gemini 2.0** multimodal model to generate a birthday wish based on the image content.

---

## Technologies Used

- **Python** (for scripting)
- **Vertex AI** (for image generation and analysis)
- **Google Cloud** (for the cloud services used in the project)
- **VS Code** (for project development)
- **Git** (for version control)

---

## Requirements

Before running the code, ensure you have the following dependencies installed:

1. **Python** 3.x (Python 3.7+ recommended)
2. **Vertex AI SDK**:
    ```bash
    pip install vertexai
    ```
3. **Google Cloud SDK**:
    ```bash
    pip install google-cloud-logging
    ```

---

## How to Run

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/repository-name.git
    cd repository-name
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python genText.py
    ```

4. You should see the output indicating that the image has been generated and analyzed, with the birthday wish being displayed.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- **Google Cloud Skills Boost** for providing the hands-on labs and challenges that inspired this project.
- **Google Cloud** for providing the Vertex AI platform.
- **Qwiklabs** for the practical labs that provided a foundation for this project.

---

## Contributing

Feel free to fork this project and submit issues or pull requests for improvements or enhancements!

