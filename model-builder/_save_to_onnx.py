import torch
from classes import BasicNetwork, CNN_1

MAJOR = 1
MINOR = 24

model = CNN_1()
# model.load_state_dict(torch.load(f"./models/{MAJOR}_{MINOR}/model_{MAJOR}_{MINOR}.pt"))
model.load_state_dict(torch.load(f"./model_{MAJOR}_{MINOR}_kat.pt"))
model.eval()
dummy_input = torch.randn(1, 1, 64, 64)
torch.onnx.export(model, dummy_input, f"model_{MAJOR}_{MINOR}_kat.onnx")
