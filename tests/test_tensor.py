import torch

tensor_a = torch.tensor([3 ,4], dtype=torch.float32)
tensor_b = torch.tensor([5 ,6], dtype=torch.float32)


print(torch.dot(tensor_a, tensor_b))