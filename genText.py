import argparse

import vertexai
from vertexai.generative_models import GenerativeModel, Part, Image

def analyze_bouquet_image(image_path: str):
    vertexai.init(
        project='PROJECT-ID',
        location='REGION',
    )
    
    multimodal_model = GenerativeModel("gemini-2.0-flash-001")
    
    messages = [
        "You are a creative assistant. A user has provided an image of a flower bouquet. Based on the appearance, colors, and mood of the bouquet in the image, write a warm and personalized birthday wish. Make the message joyful, heartfelt, and suitable for a birthday card.",
        Part.from_image(Image.load_from_file(location=image_path))
    ]

    chat = multimodal_model.start_chat()

    print(chat.send_message(content=messages, stream=False))

analyze_bouquet_image(
    image_path='image.jpeg'
)
"""root@2a0a384f10cb:/home/student# /usr/bin/python3 /genText.py
candidates {
  content {
    role: "model"
    parts {
      text: "Happy Birthday!\n\nLike this vibrant bouquet of sunflowers and roses, may your day be filled with sunshine and love. The sunflowers remind me of your radiant smile, and the roses symbolize the deep affection we all have for you. Wishing you a year ahead that\'s just as bright and beautiful as you are!\n\nWith love and best wishes,\n[Your Name]\n"
    }
  }
  finish_reason: STOP
  avg_logprobs: -0.41849861145019529
}
usage_metadata {
  prompt_token_count: 1345
  candidates_token_count: 75
  total_token_count: 1420
  prompt_tokens_details {
    modality: TEXT
    token_count: 55
  }
  prompt_tokens_details {
    modality: IMAGE
    token_count: 1290
  }
  candidates_tokens_details {
    modality: TEXT
    token_count: 75
  }
}
model_version: "gemini-2.0-flash-001"
create_time {
  seconds: 1746212845
  nanos: 193460000
}
response_id: "7RcVaLTnC6Cjz_IP5JjTkAY" """