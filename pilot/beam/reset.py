import os
from .logging import Log


def reset_beam():
    node_config = os.path.expanduser('~/.beam/node.toml')
    if os.path.exists(node_config):
        try:
            os.remove(node_config)
        except OSError as e:
            Log("Error: %s - %s." % (e.filename, e.strerror), fg="red", bold=True)
            exit(1)
    return
