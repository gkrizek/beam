from .awslambda import invoke_commander


def get_gaiad_config(type):
    config = invoke_commander({
        "action": "config_file",
        "type": type
    })
    return config


def initialize(local_ip,public_ip,moniker,type):
    # post all the info to commander
    # Then get the gaiad config from commander
    # Write or overwrite the gaiad config with the commander version
    # start gaiad
    return