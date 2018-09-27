![beam-pilot-logo.png](beam-pilot-logo.png)


Beam Pilot is a CLI Application that controls the gaiad service on a [Cosmos](https://cosmos.network) Validator or Sentry. It also communicates with the [Commander](../commander).

**Features:**

- Auto-Bounding of Steaks
- Proposal Notifications
- Auto-Voting
- Change gaiad configuration file
- Ask the Commander for assistance if getting overwhelmed
- DDoS Mitigation


### Install

_Not working yet_

```bash
pip install beam
```


### Feature Descriptions

**Auto-Bonding of Stake**

Pilot will query your Validator address with the `gaiacli account` command. If it sees that there are unbonded tokens, it will automatically bond the full amount to your Validator address.

**Proposal Notifications**

Pilot will query the most recent voting proposal on the network. If it's a new proposal, it will tell the Commander to alert you about it. When it alerts you about it, you will have the option to vote on the proposal through the application you were alerted with.

**Auto-Voting**

You can optionally turn on Auto-Voting. This will automatically cast a vote on a new proposal if the proposal is going to expire in under 1 minute and you have not yet voted on it.

**gaiad configarion file**

When a server comes online (Validator or Sentry), Pilot will check into the Commander. Commander will return a dynamically generated gaiad config file to use. This file will have the most up to date list of Persistent Peers, Validator Node, and other Sentrys.

**Commander Rescue**

Pilot will frequently query OS level stats to make sure it's not being overwhelmed. If it does report that it's being overwhelmed, Pilot will tell Commander to send in reinforments. This would be like increasing the number of servers in an Auto Scaling Group.

**DDoS Mitigation**

Pilot will also query the amount of connections and attempted connections to the server. If we start to reach higher than normal connections, then Pilot will alert the Commander about it. The Commander will then take defensive action and change the Public IP Address of the Sentry Node to mitigate a potential DDoS attack.
