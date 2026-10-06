#2. WAP to convert given text into image using pretrained GAI model
# maam's code idle

pip install diffusers accelerate
from diffusers import StableDiffusionPipeline
import torch

# Load the pre-trained Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)

# Use GPU
pipe = pipe.to("cuda")

# Generate image
prompt = "Sunrise"

image = pipe(prompt).images[0]

# Save the generated image
image.save("output.png")

print("Sunrise image is generated and saved as output.png")
