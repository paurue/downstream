# Downstream
Downstream is a seamless module for Causal Inference

## Diclaimer
Downstream is at a very early stage, and the API will most certainly undergo big changes


## Install
```bash
pip install git+git://github.com/paurue/downstream.git
```

## Use
```python
from downstream import CausalModel
model = CausalModel(""" dag {
    Treatment -> Recovery
    Treatment <- Size -> Recovery
}
"""
)
print(model)
>> CausalModel(Treatment → Recovery, Size → Treatment, Size → Recovery)
model.plot()
```
[Causal Graph](docs/images/graph.png)