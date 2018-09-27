![beam-pilot-logo.png](beam-pilot-logo.png)


Beam Pilot is a CLI Application that controls the gaiad service on a [Cosmos](https://cosmos.network) Validator or Sentry. It also communicates with the [Commander](../commander).

**Features:**

- Auto-Bounding of Steaks
- Proposal Notifications
- Auto-Voting
- Change gaiad configuration file
- Ask the Commander for assistance if getting overwhelmed
- DDoS Mitigation
- Primary/Secondary Validator Servers


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

**Primary/Secondary Validator Servers**

Because Pilot is running health checks on the server and on gaiad, we are able to tell if a Validator isn't online or behaving properly. This allows us to failover to a secondary Validator in the event that your primary server fails. If Commander sees the primary Validator go offline, it signals to the secondary Validator to get a new gaiad config and restart gaiad. This will move everything in to place for your secondary server to start Validating while you fix the other. This is also very helpful for software upgrades and maintenance. You can easily upgrade one server, then failover and upgrade the other.


### Configuration File

Beam Pilot uses a TOML file to get its configuration. The default place for this file is `~/.beam/config.toml`. This file will have everything you need to configure Pilot and turn features on or off. [Here is an example config file](configs/example-config.toml). Below are the descriptions of each value and their possible options.

**`node_type`:**

Must be either `validator` or `sentry`

**`alerting`:**

True/False to turn on or off alerts.

**`alert_type`:**

Must be either `commander` or `local`. How to send out the alerts.

**`port`:**

Any open port. This is the port the Commander uses to check on the health of the Pilot


**_Commander Section_**

**`enable`:**

True/False to turn on or off the Commander integration

**`commander`:**

The name of the Lambda function for your Commander

**`bucket`:**

The name of the S3 Bucket for your Commander


**_Validator Section_**

**`primary`:**

True/False to tell Commander if this Validator is primary or secondary

**`voting`:**

True/False to turn on or off automatic voting

**`bonding`:**

True/False to turn on or off automatic bonding of steak

**`address`:**

Your Validator's public Comsos Address


**_Sentry Section_**

**`public`:**

True/False to tell Commander if Sentry is private or public

**`connections`:**

True/False to turn on or off checking of connections for DDoS mitigation

**`defense`:**

True/False to turn on or off taking action if a DDoS attack is suspected


**_Gaiad Section_**

**`enable`:**

True/False to turn on or off Pilot controlling your gaiad install and service

**`directory`:**

Your `gaiad` directory. Default is `~/.gaiad`


### CLI Options

```
$ beam
Usage: beam [OPTIONS] COMMAND [ARGS]...

   _ )  __|    \     \  |    _ \ _ _|  |      _ \ __ __|
   _ \  _|    _ \   |\/ |    __/   |   |     (   |   |
  ___/ ___| _/  _\ _|  _|   _|   ___| ____| \___/   _|

  Beam Pilot - Cosmos Infrastructure Manager

Options:
  --help  Show this message and exit.

Commands:
  init     initialize
  reset    reset the Beam Pilot node
  start    start the agent
  status   check agent status
  version  check agent version
```