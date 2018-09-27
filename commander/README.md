![beam-commander-logo.png](beam-commander-logo.png)

Beam Commander is a serverless application that runs in AWS Lambda. It is written to be used with [Beam Pilot](../pilot) to control and communicate with your [Cosmos](https://cosmos.network) Validator Architecture.

**Features:**

- Alert to various messaging endpoints
- Failover Validator Nodes
- Change the public IP address for a server under distress
- Generate dynamic gaiad configuration files
- Check health of all Validator and Sentry servers



### Allowed Actions

- `healthcheck`
- `config_file`
- `list`
- `report`

**Required Environment Variables:**

- COMMANDER_S3_BUCKET
- COMMANDER_CHECK_INTERVAL (optional)
