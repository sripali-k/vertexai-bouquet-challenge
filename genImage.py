import argparse

import vertexai
from vertexai.preview.vision_models import ImageGenerationModel

def generate_bouquet_image(
    prompt: str
) -> vertexai.preview.vision_models.ImageGenerationResponse:

    vertexai.init(
        project='qwiklabs-gcp-01-cc0666c6f72b',
        location='europe-west4',
    )

    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-002")

    images = model.generate_images(
        prompt=prompt,
        # Optional parameters
        number_of_images=1,
        seed=1,
        add_watermark=False,
    )

    images[0].save(location='image.jpeg')

    return images


generate_bouquet_image(
    prompt='Create an image containing a bouquet of 2 sunflowers and 3 roses',
)