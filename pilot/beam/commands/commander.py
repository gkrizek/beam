

def commander_checkin(local_ip,public_ip,moniker,type):
    # Checkin to Commander lambda function
    return 'bb554433aadd'


def get_orders():
    '''
    This is calling the commander lambda function to see if there are any changes that I need.
    This will return with what needs to happen if anything and information about itself.
    example response:
    {
        "action": "none"
    }

    {
        "action": "config-update",
        "file": "bucket/folder/file.toml"
    }
    '''
    return
