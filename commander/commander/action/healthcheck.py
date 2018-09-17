from time import sleep

SLEEP_TIME = 3

def HealthCheck(body):

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
            sleep(SLEEP_TIME)