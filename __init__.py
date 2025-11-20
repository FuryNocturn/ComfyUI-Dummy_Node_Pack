from .nodes import Fake_ECHOCheckpointLoaderSimple, Fake_KSampler_A1111

# Aquí mapeamos el NOMBRE INTERNO (el que busca ComfyUI en el json) con nuestra CLASE FAKE.
# Si necesitas añadir más nodos, impórtalos arriba y añádelos a este diccionario.

NODE_CLASS_MAPPINGS = {
    "ECHOCheckpointLoaderSimple": Fake_ECHOCheckpointLoaderSimple,
    "KSampler_A1111": Fake_KSampler_A1111,
    # "NombreDelNodoFaltante": ClaseFakeNueva,
}

# Estos son los nombres que verás tú en la interfaz visual.
NODE_DISPLAY_NAME_MAPPINGS = {
    "ECHOCheckpointLoaderSimple": "🛑 DUMMY ECHO Loader",
    "KSampler_A1111": "🛑 DUMMY KSampler A1111",
    # "NombreDelNodoFaltante": "🛑 DUMMY Nombre",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']