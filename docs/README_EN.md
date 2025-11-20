# 🧩 ComfyUI Dummy Node Pack

![License](https://img.shields.io/badge/License-MIT-green.svg) ![Platform](https://img.shields.io/badge/Platform-ComfyUI-blue)

[Español](README.md) | [English](README_EN.md) | [Deutsch](README_DE.md) | [Русский](README_RU.md) | [中文](README_CN.md) | [日本語](README_JP.md)

---

**Regain control of your Workflows.**

This custom node pack creates "Fake Nodes" to replace old, deleted, or cloud-service-specific nodes (like A1111, Cloud, etc.) that prevent a workflow from loading in ComfyUI.

> ⚠️ **IMPORTANT:** These nodes **DO NOT process images**. They are *placeholders* that allow the graph to load visually without errors, preserving the connections (wires) so you can replace them with functional native nodes.

---

## 🚀 Why use this?

When you load an old workflow and nodes are missing, ComfyUI often breaks the interface or prevents execution.
This pack solves the "Chicken and Egg" problem:
1.  Loads missing nodes as "Dummies".
2.  Allows you to see where the wires were connected.
3.  Gives you the opportunity to connect native nodes (`Load Checkpoint`, `KSampler`, etc.).
4.  Once fixed, you can delete the dummies.

### Visual Example

![Example workflow loaded with Dummy nodes (highlighted in red boxes), maintaining original connections.](image_0.png)
*Example workflow loaded with Dummy nodes (highlighted in the red boxes), maintaining original connections for easy replacement.*

---

## 📋 Currently Supported Nodes

If your flow requires any of these nodes, this pack will automatically load it as a 🛑 **DUMMY** node.

| Missing Node Name (ID) | Description / Original Use | Solution (Replace with Natives) |
| :--- | :--- | :--- |
| `ECHOCheckpointLoaderSimple` | Simple model loader | **Load Checkpoint** |
| `KSampler_A1111` | Automatic1111 style sampler | **KSampler** (Copy seed/steps values) |

---

## 🛠️ Installation

1.  Go to your `ComfyUI/custom_nodes/` folder.
2.  Clone this repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/ComfyUI-Dummy_Node_Pack.git](https://github.com/YOUR_USERNAME/ComfyUI-Dummy_Node_Pack.git)
    ```
3.  Restart ComfyUI.

---

## 🧑‍💻 Development Guide: How to add more nodes

The structure is designed to be **modular**. If you download a new flow and are missing a different node (e.g., `SuperUpscaler`), follow these steps to add it to your local pack:

### Step 1: Define the Node
Open the `nodes.py` file. Copy the template at the end and adapt it. The important thing is to define the `INPUT_TYPES` to match the wires you need to rescue.

```python
# In nodes.py
class Fake_SuperUpscaler:
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        # Define here the inputs the original node had
        return {"required": { "image": ("IMAGE",), "scale": ("FLOAT", {"default": 1.5}) }}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_nothing"
    CATEGORY = "Dummy Pack"

    def do_nothing(self, **kwargs): return (None,)
```

### Step 2: Register the Node
Open the __init__.py file, import your new class, and add it to the mapping:

```python
# In __init__.py
from .nodes import Fake_ECHOCheckpointLoaderSimple, Fake_KSampler_A1111, Fake_SuperUpscaler # <--- 1. Import

NODE_CLASS_MAPPINGS = {
    "ECHOCheckpointLoaderSimple": Fake_ECHOCheckpointLoaderSimple,
    "KSampler_A1111": Fake_KSampler_A1111,
    "SuperUpscaler": Fake_SuperUpscaler # <--- 2. Map the exact missing name
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SuperUpscaler": "🛑 DUMMY SuperUpscaler" # <--- 3. Visible name in UI
}
```

### Step 3: Apply
Restart ComfyUI and load your flow. Done!

## 📄 License
This project is under the MIT license. You are free to use, modify, and share it.