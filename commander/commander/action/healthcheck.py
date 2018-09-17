from time import sleep


def HealthCheck(body):

    try:
        check_interval = os.environ['COMMANDER_CHECK_INTERAL']
    except KeyError:
        check_interval = 5

    while True:

        # TODO Find out how many seconds left in execution
        # This is if 5 seconds left in execution allocation, terminate.
        execution_time = 120
        if execution_time < 5:
            return {
                'statusCode': 200,
                'body': 'Completed Health Checks'
            }
        else:

            # TODO: Run the checks
            sleep(check_interval)