![beam-logo.png](beam-logo.png)

Beam is aimed to be a full-service management tool for running a [Cosmos](https://cosmos.network) Validator. Beam enables you to run a highly available and secure Validator behind a dynamic set of Sentrys. The Beam project comes in two pieces, Beam Pilot and Beam Commander. Beam Pilot is a tool to be installed on your servers, while Beam Commander is a Lambda Function that communicates with all the Pilots. Beam is designed to handle all the needs of running a dynamic Validator architecure without manual processes.

_While Pilot can be installed on any server, Commander is written to only be ran in AWS Lambda. Therefore, there is a requirement that this tool only be ran in [AWS](https://aws.amazon.com)._

## Beam Pilot

Pilot is a tool that installs onto your Sentry and Validator servers. It can be used to control the server, as well as talk to the Commander.

See the [Pilot directory](./pilot) for more information.
Ok 
## Beam Commander

Commander is a Lambda function that controls and talks to all of the Pilots.

See the [Commander directory](./commander) for more information.

## Getting Started

To learn how to get started with Beam, see the [GETTING-STARTED.md](GETTING-STARTED.md) file.

## Beam Infrastructure

The [Infrastructure directory](./infrastructure) contains a collection of [Terraform](https://terraform.io) templates to be used as examples on how to create a compatible Beam architecture.


### Architecture Diagram

![beam-arch.png](beam-arch.png)

#### Maintainer

[Graham Krizek](https://github.com/gkrizek)

