import torch
from classes import BasicNetwork
import nobuco
from nobuco import ChannelOrder, ChannelOrderingStrategy
from nobuco.layers.weight import WeightLayer


model = BasicNetwork()
model.load_state_dict(torch.load("best_go.pt"))
dummy_input = torch.randn(1, 1, 64, 64)
pytorch_module = model().eval()

keras_model = nobuco.pytorch_to_keras(
    pytorch_module,
    args=[dummy_input],
    inputs_channel_order=ChannelOrder.TENSORFLOW,
    outputs_channel_order=ChannelOrder.TENSORFLOW,
)
