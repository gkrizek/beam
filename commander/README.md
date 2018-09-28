![beam-commander-logo.png](beam-commander-logo.png)

Beam Commander is a serverless application that runs in AWS Lambda. It is written to be used with [Beam Pilot](../pilot) to control and communicate with your [Cosmos](https://cosmos.network) Validator Architecture.

**Features:**

- Alert to various messaging endpoints
- Failover Validator Nodes
- Change the public IP address for a server under distress
- Generate dynamic gaiad configuration files
- Check health of all Validator and Sentry servers


### Feature Descriptions

**Alerting**

Commander has the ability to hook into several messaging services like Telegram, Slack, and SMS. When something happens in your infrastructure that you should know about, it tells you.

**Failover Validator Nodes**

When the Pilot node_type is a Validator, Pilot is constantly checking an endpoint to ensure it is behaving in the right way. If the primary validator goes offline, Commander will see that and tell your Secondary Validator to start. This will allow you to never miss a block even if your server goes down. This can also be used for manual failover when updating software.

**Change Public IP**

Commander is designed to be run in AWS along with your Sentrys. Because Sentrys are EC2 instances, they can have Elastic IP Addresses. When a Pilot server signals to the Commander that it is being overwhelmed (possibly from DDoS), the Commander will replace it's public IP with a new one. This will affectively stop the attack and allow the Sentry to restablish connections with good nodes on the network.

**Dynamic gaiad config**

Commander keeps a list of all the nodes in your architecture and what their purpose is. Because of this, Commander can dynamically generate gaiad config files for you and have the proper settings enabled/disabled. Such as `private_peers`, `persistent_peers`, `pex`, etc. This means that you infrastructure can be highly dynamic and fluid without needing manual changes all the time.

**Health Checks**

Every Pilot server has an HTTP server running on it displaying its health status. Since Commander keeps a list of all nodes, we frequently check on the health status of all servers. If there is a problem, Commander will handle it in the appropriate way.



### Allowed Actions

- `healthcheck`
- `config_file`
- `list`
- `report`

**Required Environment Variables:**

- COMMANDER_S3_BUCKET
- COMMANDER_CHECK_INTERVAL (optional)
