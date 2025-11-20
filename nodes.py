import torch

class Fake_ECHOCheckpointLoaderSimple:
    """
    Simula el nodo ECHOCheckpointLoaderSimple.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "ckpt_name": ("STRING", {"default": "fake_model.safetensors"}),
            }
        }

    RETURN_TYPES = ("MODEL", "CLIP", "VAE")
    RETURN_NAMES = ("MODEL", "CLIP", "VAE")
    FUNCTION = "do_nothing"
    CATEGORY = "Dummy Pack"

    def do_nothing(self, **kwargs):
        return (None, None, None)

class Fake_KSampler_A1111:
    """
    Simula el nodo KSampler_A1111.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "seed": ("INT", {"default": 0, "min": 0, "max": 0xffffffffffffffff}),
                "steps": ("INT", {"default": 20, "min": 1, "max": 10000}),
                "cfg": ("FLOAT", {"default": 8.0, "min": 0.0, "max": 100.0}),
                "sampler_name": ("STRING", {"default": "euler"}),
                "scheduler": ("STRING", {"default": "normal"}),
                "positive": ("CONDITIONING",),
                "negative": ("CONDITIONING",),
                "latent_image": ("LATENT",),
                "denoise": ("FLOAT", {"default": 1.0, "min": 0.0, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("LATENT",)
    FUNCTION = "do_nothing"
    CATEGORY = "Dummy Pack"

    def do_nothing(self, **kwargs):
        return (None,)

# ---------------------------------------------------------------------------
#  PLANTILLA PARA AÑADIR NUEVOS NODOS EN EL FUTURO
# ---------------------------------------------------------------------------
# Para añadir otro nodo, copia la clase de abajo, cámbiale el nombre
# y define sus INPUT_TYPES para que coincidan con los cables que necesitas conectar.
#
# class Fake_NOMBRE_DEL_NODO_FALTANTE:
#     def __init__(self): pass
#     @classmethod
#     def INPUT_TYPES(s):
#         return {"required": { "input_dummy": ("STRING", {"default": ""}) }}
#     RETURN_TYPES = ("STRING",)
#     FUNCTION = "do_nothing"
#     CATEGORY = "Dummy Pack"
#     def do_nothing(self, **kwargs): return (None,)