![beam-logo.png](files/beam-logo.png)

_Beam is being created as part of the [HackAtom3 Hackathon](https://blog.cosmos.network/announcement-hackatom3-is-live-83c3492a45e5). Therefore it is still a Work in Progress and not functional at this time._

Beam is aimed to be a full-service management tool for running a [Cosmos](https://cosmos.network) Validator. Beam enables you to run a highly available and secure Validator behind a dynamic set of Sentrys. The Beam project comes in two pieces, Beam Pilot and Beam Commander. Beam Pilot is a tool to be installed on your servers, while Beam Commander is a Lambda Function that communicates with all the Pilots. Beam is designed to handle all the needs of running a dynamic Validator architecure without manual processes.

_While Pilot can be installed on any server, Commander is written to only be ran in AWS Lambda. Therefore, there is a requirement that this tool only be ran in [AWS](https://aws.amazon.com)._

## Highlights:

- Primary/Secondary Validator with automatic failover
- DDoS Protection via automatic IP changes
- Dynamic Gaiad Configuration Management
- Auto-Bonding of Steak
- Governance Proposal Alerts
- Auto-Voting based on timed thresholds
- Infrastructure Health Checks

**How It Works**

Beam Pilot is installed on all servers, Validators and Sentrys. Beam Pilot is running constantly and it will manage your gaiad service for you. Pilot will bootstrap your gaiad config by asking Commander for the config. Commander keeps a running list of nodes and will constantly update it's template gaiad config. Pilot checks the status on gaiad, network, server health, and more. If Pilot detects a change that requires action, it takes the proper action. For example, if Pilot notices that you have new Steak on your Validator address that isn't bonded yet, it will bond the Steak for you. It can also monitor for new governance proposals and alert you if there is a new one. Pilot puts most of these stats into an HTTP endpoint that is queryable from the Commander. The Commander is a Lambda function that runs at a given interval to monitor all servers. If it sees a server is offline, it will failover to a secondary (for validators) or terminate the instance for replacement (for sentrys). Commander is able to interact with administrators via external APIs as well. This enables things like Alert notifications, Sending in votes from Slack/Telegram, server edits, etc. When Commander queries Pilots it is able to act on their responses. For example, if a Sentry is starting to get overwhelmed, Commander will stop gaiad, change its Public IP (and gaiad config), then start gaiad. This is a method of defense against unwanted connections.

Beam is made to bring automation into all aspects for running a Cosmos Validator. Through automation, Validators are easier to operated and more stable.

### Beam Pilot

Pilot is a tool that installs onto your Sentry and Validator servers. It can be used to control the server, as well as talk to the Commander. The Pilot will gather information from gaiad, the server, and the Cosmos Network. Then it will act on that information based on what is appropriate. 

Examples of actions are:

- Auto-Bonding of Stake
- Alert on a new Proposal
- Auto-Voting
- Change gaiad configuration file
- Ask the Commander for assistance if getting overwhelmed
- Primary/Secondary Validator servers

_Pilot can be ran with or without a Commander, however a lot of features are lost without a Commander._

See the [Pilot directory](./pilot) for more information.


### Beam Commander

Commander is a Lambda function that controls and talks to all of the Pilots. The Commander runs a check at a given interval to check on all connected Pilots. If a Pilot has something that needs to be done, the Commander takes will execute that action. If a Pilot fails health checks, the Commander will replace it. The Commander will also generate dynamic gaiad configuration files for the Pilots to use so all servers are up to date.

Examples of actions are:

- Alert to various messaging endpoints
- Failover Validator Nodes
- Change the public IP address for a server under distress
- Generate dynamic gaiad configuration files
- Check health of all Validator and Sentry servers

See the [Commander directory](./commander) for more information.


### Beam Infrastructure

The [Infrastructure directory](./infrastructure) contains a collection of [Terraform](https://terraform.io) templates to be used as examples on how to create a compatible Beam architecture.


#### Architecture Diagram

![beam-arch.png](files/beam-arch.png)


#### Maintainer

[Graham Krizek](https://github.com/gkrizek)

