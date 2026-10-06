#2. WAP to convert given text into image using pretrained GAI model
# maam's code idle

# Step 1: Install required libraries
!pip install -q diffusers accelerate transformers torch

# Step 2: Import libraries
from diffusers import StableDiffusionPipeline
import torch

# Step 3: Check GPU
gpu_available = torch.cuda.is_available()
print("GPU available:", gpu_available)

# Dynamically select device and precision based on GPU availability
device = "cuda" if gpu_available else "cpu"
torch_dtype = torch.float16 if gpu_available else torch.float32

# Step 4: Load the pre-trained Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch_dtype
)

# Step 5: Move to appropriate device
pipe = pipe.to(device)

# Step 6: Generate image
prompt = "Sunrise over beach, beautiful sky, realistic"
image = pipe(prompt).images[0]

# Step 7: Save the image
image.save("output.png")

# Step 8: Display the image
display(image)

print("Image generated successfully!")
