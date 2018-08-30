# Beam

Beam is a management tool for running a [Cosmos](https://cosmos.network) Validator. Beam enables you to run a highly available and secure Validator. It is designed to be used with a transient environment.

While Pilot can be installed in any cloud, Commander is written to only be ran in AWS Lambda. Therefore, there is a requirement that this tool only be ran in AWS.

## Beam Pilot

Pilot is a tool that installs onto your Sentry and Validator servers. It can be used to control the server, as well as talk to the Commander.

See the [Pilot directory](./pilot) for more information.

## Beam Commander

Commander is a Lambda function that controls and talks to all of the Pilots.

See the [Commander directory](./commander) for more information.

## Beam Infrastructure

The [Infrastructure directory](./infrastructure) contains a collection of [Terraform](https://terraform.io) templates to be used as examples on how to create a compatible Beam architecture.
