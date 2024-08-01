from pathlib import Path


def list_templates(script_dir):
    templates = [d.name for d in (script_dir / 'templates').iterdir() if d.is_dir()]
    print("Available structure types:")
    print(", ".join(templates))