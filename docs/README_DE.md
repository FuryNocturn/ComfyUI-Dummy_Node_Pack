# 🧩 ComfyUI Dummy Node Pack (Dummy-Knotenpaket)

![License](https://img.shields.io/badge/License-MIT-green.svg) ![Platform](https://img.shields.io/badge/Platform-ComfyUI-blue)

[Español](README.md) | [English](README_EN.md) | [Deutsch](README_DE.md) | [Русский](README_RU.md) | [中文](README_CN.md) | [日本語](README_JP.md)

---

**Gewinnen Sie die Kontrolle über Ihre Workflows zurück.**

Dieses Paket benutzerdefinierter Knoten erstellt "Fake-Knoten" (simulierte Knoten), um alte, gelöschte oder Cloud-Service-spezifische Knoten (wie A1111, Cloud usw.) zu ersetzen, die das Laden eines Workflows in ComfyUI verhindern.

> ⚠️ **WICHTIG:** Diese Knoten **verarbeiten KEINE Bilder**. Es sind *Platzhalter*, die es ermöglichen, den Graphen visuell ohne Fehler zu laden und die Verbindungen (Kabel) beizubehalten, damit Sie sie durch funktionale native Knoten ersetzen können.

---

## 🚀 Warum dies verwenden?

Wenn Sie einen alten Workflow laden und Knoten fehlen, bricht ComfyUI oft die Benutzeroberfläche oder verhindert die Ausführung.
Dieses Paket löst das "Henne-Ei"-Problem:
1.  Lädt fehlende Knoten als "Dummies".
2.  Ermöglicht es Ihnen zu sehen, wohin die Kabel führten.
3.  Gibt Ihnen die Möglichkeit, native Knoten zu verbinden (`Load Checkpoint`, `KSampler` usw.).
4.  Sobald repariert, können Sie die Dummies löschen.

### Visuelles Beispiel

![Beispiel-Workflow, geladen mit Dummy-Knoten (in roten Boxen hervorgehoben), wobei die ursprünglichen Verbindungen beibehalten werden.](image_0.png)
*Beispiel-Workflow, geladen mit Dummy-Knoten (in den roten Boxen hervorgehoben), wobei die ursprünglichen Verbindungen für einen einfachen Austausch beibehalten werden.*

---

## 📋 Derzeit unterstützte Knoten

Wenn Ihr Workflow einen dieser Knoten benötigt, lädt dieses Paket ihn automatisch als 🛑 **DUMMY**-Knoten.

| Name des fehlenden Knotens (ID) | Beschreibung / Ursprüngliche Verwendung | Lösung (Durch Natives ersetzen) |
| :--- | :--- | :--- |
| `ECHOCheckpointLoaderSimple` | Einfacher Modell-Loader | **Load Checkpoint** |
| `KSampler_A1111` | Sampler im Automatic1111-Stil | **KSampler** (Seed/Steps-Werte kopieren) |

---

## 🛠️ Installation

1.  Gehen Sie zu Ihrem Ordner `ComfyUI/custom_nodes/`.
2.  Klonen Sie dieses Repository:
    ```bash
    git clone [https://github.com/IHR_BENUTZERNAME/ComfyUI-Dummy_Node_Pack.git](https://github.com/IHR_BENUTZERNAME/ComfyUI-Dummy_Node_Pack.git)
    ```
3.  Starten Sie ComfyUI neu.

---

## 🧑‍💻 Entwicklerhandbuch: Wie man weitere Knoten hinzufügt

Die Struktur ist **modular** aufgebaut. Wenn Sie einen neuen Workflow herunterladen und ein anderer Knoten fehlt (z. B. `SuperUpscaler`), befolgen Sie diese Schritte, um ihn zu Ihrem lokalen Paket hinzuzufügen:

### Schritt 1: Den Knoten definieren
Öffnen Sie die Datei `nodes.py`. Kopieren Sie die Vorlage am Ende und passen Sie sie an. Wichtig ist, die `INPUT_TYPES` so zu definieren, dass sie mit den Kabeln übereinstimmen, die Sie retten müssen.

```python
# In nodes.py
class Fake_SuperUpscaler:
    def __init__(self): pass

    @classmethod
    def INPUT_TYPES(s):
        # Definieren Sie hier die Eingänge, die der ursprüngliche Knoten hatte
        return {"required": { "image": ("IMAGE",), "scale": ("FLOAT", {"default": 1.5}) }}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "do_nothing"
    CATEGORY = "Dummy Pack"

    def do_nothing(self, **kwargs): return (None,)
	```
	
### Schritt 2: Den Knoten registrieren
Öffnen Sie die Datei __init__.py, importieren Sie Ihre neue Klasse und fügen Sie sie dem Mapping hinzu:

```python
# In __init__.py
from .nodes import Fake_ECHOCheckpointLoaderSimple, Fake_KSampler_A1111, Fake_SuperUpscaler # <--- 1. Importieren

NODE_CLASS_MAPPINGS = {
    "ECHOCheckpointLoaderSimple": Fake_ECHOCheckpointLoaderSimple,
    "KSampler_A1111": Fake_KSampler_A1111,
    "SuperUpscaler": Fake_SuperUpscaler # <--- 2. Den exakten fehlenden Namen zuordnen
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SuperUpscaler": "🛑 DUMMY SuperUpscaler" # <--- 3. Sichtbarer Name in der UI
}
```
### Schritt 3: Anwenden
Starten Sie ComfyUI neu und laden Sie Ihren Workflow. Fertig!

## 📄 Lizenz
Dieses Projekt steht unter der MIT-Lizenz. Es steht Ihnen frei, es zu verwenden, zu ändern und zu teilen.