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
        "Generate a birthday wish based on the following image",
        Part.from_image(Image.load_from_file(location=image_path))
    ]

    chat = multimodal_model.start_chat()

    print(chat.send_message(content=messages, stream=False))

analyze_bouquet_image(
    image_path='image.jpeg'
)
""" #root@0ce112e7ef3f:/home/student# /usr/bin/python3 /genText.py
candidates {
  content {
    role: "model"
    parts {
      text: "Happy Birthday! May your day be as bright and cheerful as a sunflower, and filled with as much love and beauty as a red rose. Wishing you a truly wonderful day!\n"
    }
  }
  finish_reason: STOP
  avg_logprobs: -0.43720875846015084
}
usage_metadata {
    prompt_token_count: 1299
  candidates_token_count: 36
  total_token_count: 1335
  prompt_tokens_details {
       modality: IMAGE
    token_count: 1290
  }
  prompt_tokens_details {
    modality: TEXT
    token_count: 9
  }
  candidates_tokens_details {
    modality: TEXT
    token_count: 36
  }
  }
model_version: "gemini-2.0-flash-001"
create_time {
  seconds: 1746203281
  nanos: 176822000
}
response_id: "kfIUaLblCriamecPiu7i0Ag"
        

         """