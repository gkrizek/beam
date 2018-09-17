# List of TODOs & Ideas

- Log Management

- Multple Alert targets

- Gaiad Version Update support

- Force failover of Validator for upgrades

- Be able to respond to voting in Slack/Telegram

- Have all beam pilots check into commander at a given internal. Then we can alert from Commander if a host goes offline unexpectedly.

- Analyize log files to see things like missed blocks, connection errors, etc. 

- Faster bootstrapping

- Need to add timestamps to logs

- Scaling up should be easy, but how do I scale down?

- Health checks:

```
Maybe what I can do for health checks is to have a list of nodes in S3 for the commander to access. Every X seconds, a Lambda function makes an HTTP request to all the nodes. If one doesn't repond, handle it appropriately. This would require creating an HTTP agent in the beam pilot.  Also, when a new server is spun up, part of initialization would be to tell Commander its IP address and it gets added to the node list. If a server doesn't respond, then terminate it, remove it from the list, and replace it.
```

- For the HTTP Status Check, maybe we should write the metrics to a file every time beam runs. Then that http endpoint can return status info as well.

- For Alerting, maybe allow two types of alerts, commander or local. If local, try to send messages somehow from the server. If commander, invoke the lambda function and alert from there. This will allow for much more alerting options, but still have basic alerting if you dont want to run commander.


---

## Notes

```
The pilot command line tool can ran by itself (no commander lambda function) or with a connection to a commander lambda function.

When a server starts up, it will first run `beam init` and the `beam start`. This will create a '~/.beam/node.toml' file and start beam. It will then check in to the commander lambda function (if enabled) and get it's gaiad config. The gaiad data directory should already by present because of a mounted EBS volume from a snapshot. Then it starts gaiad and monitors it.

For Sentry servers, the only other time it communicate with the commander server is if it posts an event to it, such as a voting alert, ddos attach, etc.

For Validator servers,... figure out what to do about validators, but they will have some sort of health check running on them. If the checks fail, we trigger beam to start the next secondary validator. This means that the validator beam programs will need to check into the commander function every X seconds to see if there is something to do.

Nodes know about each other by making a request directly to one another with the gaiad RPC endpoints. Commander is also always updating the template gaiad config so it's recent.
# How do nodes know the ips of the others? should I keep an updated list of them on the server in the node.toml file? Should I just make a lambda call to request them?

*** I think instead of terminating the whole instance if it gets DDoSed, we should just change its elastic IP address. So we could stop gaiad, switch EIP, then start gaiad. Don't have to worry about size of the blockchain weighing us down. We would still need to do regular backups of the blockchain for fast bootstrapping, but not as much of a requirement as perviously. 

---

* 15GB of data on a 30GB ebs volume - 17 min snapshot

* Need to test running a full node in a private subnet and getting internet through NAT. Put a fake public ip in the config
```