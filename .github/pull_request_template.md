## What
*Describe what the change is solving*

## How
*Describe the solution*

## Recommended reading order
1. `x.java`
2. `y.python`

## 🚨 User Impact 🚨
Are there any breaking changes? What is the end result perceived by the user? If yes, please merge this PR with the 🚨🚨 emoji so changelog authors can further highlight this if needed.

## Pre-merge Checklist
Expand the relevant checklist and delete the others.

<details><summary><strong>New Connector</strong></summary>

- [ ] Secrets in the connector's spec are annotated with `airbyte_secret`
- [ ] Unit & integration tests added and passing. Community members, please provide proof of success locally e.g: screenshot or copy-paste unit, integration, and acceptance test output. To run acceptance tests for a Python connector, follow instructions in the README. For java connectors run `./gradlew :airbyte-integrations:connectors:<name>:integrationTest`.
- [ ] Code reviews completed
- [ ] Documentation updated
    - [ ] Connector's `README.md`
    - [ ] Connector's `bootstrap.md`. See [description and examples](https://docs.google.com/document/d/1ypdgmwmEHWv-TrO4_YOQ7pAJGVrMp5BOkEVh831N260/edit?usp=sharing)
    - [ ] `docs/integrations/<source or destination>/<name>.md` including changelog. See changelog [example](https://docs.airbyte.io/integrations/sources/stripe#changelog)
    - [ ] `docs/integrations/README.md`
    - [ ] `airbyte-integrations/builds.md`
- [ ] PR name follows [PR naming conventions](https://docs.airbyte.io/contributing-to-airbyte/updating-documentation#issues-and-pull-requests)

</details>

<details><summary><strong>Updating a connector</strong></summary>

- [ ] Secrets in the connector's spec are annotated with `airbyte_secret`
- [ ] Unit & integration tests added and passing. Community members, please provide proof of success locally e.g: screenshot or copy-paste unit, integration, and acceptance test output. To run acceptance tests for a Python connector, follow instructions in the README. For java connectors run `./gradlew :airbyte-integrations:connectors:<name>:integrationTest`.
- [ ] Code reviews completed
- [ ] Documentation updated
    - [ ] Connector's `README.md`
    - [ ] Connector's `bootstrap.md`. See [description and examples](https://docs.google.com/document/d/1ypdgmwmEHWv-TrO4_YOQ7pAJGVrMp5BOkEVh831N260/edit?usp=sharing)
    - [ ] Changelog updated in `docs/integrations/<source or destination>/<name>.md` including changelog. See changelog [example](https://docs.airbyte.io/integrations/sources/stripe#changelog)
- [ ] PR name follows [PR naming conventions](https://docs.airbyte.io/contributing-to-airbyte/updating-documentation#issues-and-pull-requests)

</details>

## Tests

<details><summary><strong>Unit</strong></summary>

*Put your unit tests output here.*

</details>

<details><summary><strong>Integration</strong></summary>

*Put your integration tests output here.*

</details>

<details><summary><strong>Acceptance</strong></summary>

*Put your acceptance tests output here.*

</details>