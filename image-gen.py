from openai import OpenAI
# Read from the .env file
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="a van gogh painting of a 78 year old sindhi woman with beautiful silvery hair in a ponytail. set the background as the himalayas with the kashmir dal lake.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)