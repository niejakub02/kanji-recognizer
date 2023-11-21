import torch
from classes import BasicNetwork

model = BasicNetwork()
model.load_state_dict(torch.load("best_go.pt"))
model.eval()
dummy_input = torch.randn(1, 1, 64, 64)
torch.onnx.export(model, dummy_input, "best_go.onnx")
