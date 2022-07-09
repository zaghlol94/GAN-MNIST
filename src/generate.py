import torch
import matplotlib.pyplot as plt
from config import config
from generator import Generator

device = "cuda" if torch.cuda.is_available() else "cpu"
with torch.no_grad():
    noise = torch.randn(1, config["z_dim"]).to(device)
    gen = Generator(config["z_dim"], config["image_dim"]).to(device)
    gen.load_state_dict(torch.load("gen.pt"))
    image = gen(noise)
    print(image.shape)
    print(image.shape)
    plt.imshow(image.to("cpu").squeeze().reshape(28, 28))
    plt.show()
