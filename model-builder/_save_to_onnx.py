import torch
from classes import BasicNetwork

model = BasicNetwork()
model.load_state_dict(torch.load("model_1_7.pt"))
model.eval()
dummy_input = torch.randn(1, 1, 64, 64)
torch.onnx.export(model, dummy_input, "model_1_7.onnx")
