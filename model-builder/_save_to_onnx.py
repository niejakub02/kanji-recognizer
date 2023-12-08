import torch
from classes import BasicNetwork

MAJOR = 1
MINOR = 11

model = BasicNetwork()
model.load_state_dict(torch.load(f"./models/{MAJOR}_{MINOR}/model_{MAJOR}_{MINOR}.pt"))
model.eval()
dummy_input = torch.randn(1, 1, 64, 64)
torch.onnx.export(model, dummy_input, f"model_{MAJOR}_{MINOR}.onnx")
