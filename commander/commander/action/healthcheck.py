import os
from time import sleep
from ..nodes import GetSentryIps(), GetValidatorIps()
from ..checks import CheckHealth()

def HealthCheck(body, context):

    try:
        check_interval = os.environ['COMMANDER_CHECK_INTERAL']
    except KeyError:
        check_interval = 5

    while True:
        # Check how many milliseconds are left in function execution
        time_remaining = context.get_remaining_time_in_millis()
        # if less than 5 seconds left, complete.
        if time_remaining < 5000:
            return {
                'statusCode': 200,
                'body': 'Completed Health Checks'
            }
        else:
            '''
            Types of health status:
            - healthy
            - warning
            - ddos
            - offline
            '''
            sentrys = GetSentryIps()
            for s in sentrys:
                health = CheckHealth(s)

                if health['status'] != 'healthy':
                    # TODO, what do I do if something unhealthy

            validators = GetValidatorIps()
            for v in validators:
                health = CheckHealth(v)

                if health['status'] != 'healthy':
                    # TODO, what do I do if something unhealthy



            sleep(check_interval)
