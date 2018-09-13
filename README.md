![beam-logo.png](beam-logo.png)

Beam is a management tool for running a [Cosmos](https://cosmos.network) Validators Architecture. Beam enables you to run a highly available and secure Validator. It is designed to be used with a [transient environment](commander/README.md#transient).

_While Pilot can be installed in any cloud, Commander is written to only be ran in AWS Lambda. Therefore, there is a requirement that this tool only be ran in AWS._

## Beam Pilot

Pilot is a tool that installs onto your Sentry and Validator servers. It can be used to control the server, as well as talk to the Commander.

See the [Pilot directory](./pilot) for more information.

## Beam Commander

Commander is a Lambda function that controls and talks to all of the Pilots.

See the [Commander directory](./commander) for more information.

## Beam Infrastructure

The [Infrastructure directory](./infrastructure) contains a collection of [Terraform](https://terraform.io) templates to be used as examples on how to create a compatible Beam architecture.


#### Maintainer

[Graham Krizek](https://github.com/gkrizek)


```
NOTES:

The pilot command line tool can ran by itself (no commander lambda function) or with a connection to a commander lambda function.

When a server starts up, it will first run `beam init` and the `beam start`. This will create a '~/.beam/node.toml' file and start beam. It will then check in to the commander lambda function (if enabled) and get it's gaiad config. The gaiad data directory should already by present because of a mounted EBS volume from a snapshot. Then it starts gaiad and monitors it.

For Sentry servers, the only other time it communicate with the commander server is if it posts an event to it, such as a voting alert, ddos attach, etc.

For Validator servers,... figure out what to do about validators, but they will have some sort of health check running on them. If the checks fail, we trigger beam to start the next secondary validator. This means that the validator beam programs will need to check into the commander function every X seconds to see if there is something to do.

Nodes know about each other by making a request directly to one another with the gaiad RPC endpoints. Commander is also always updating the template gaiad config so it's recent.
# How do nodes know the ips of the others? should I keep an updated list of them on the server in the node.toml file? Should I just make a lambda call to request them?

Need to add timestamps to logs

# Unknowns

- Validator Health Checks
- How to do alerting. In lambda? On server? What service?
- Probably need health checks for all sentry/validators.
- Scaling up should be easy, but how do I scale down?

## Maybe what I can do for health checks is to have a list of nodes in S3 for the commander to access. Every X seconds, a Lambda function makes an HTTP request to all the nodes. If one doesn't repond, handle it appropriately. This would require creating an HTTP agent in the beam pilot.  Also, when a new server is spun up, part of initialization would be to tell Commander its IP address and it gets added to the node list. If a server doesn't respond, then terminate it, remove it from the list, and replace it.


'''
first check how many unbonded steaks you have... with `gaiacli account <your_cosmosaccaddr...>`

then delegate to yourself with...

gaiacli stake delegate --amount=10steak  --address-delegator=<your_cosmosaccaddr...>  --address-validator=<your_cosmosaccaddr...> --from=<your_monikor>  --chain-id=gaia-8001 --gas=20000000 --async=true
'''
```
