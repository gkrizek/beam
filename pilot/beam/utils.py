import os


def config_exists():
    beam_config = os.path.expanduser('~/.beam/config.toml')
    if os.path.exists(beam_config):
        return True
    else:
        return False
