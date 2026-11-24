# The Postmortem That Made Us Laugh

[![make.fun](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![rank](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reren-dev/postmortem-laugh-01/rank.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)
[![reward](https://make.fun/badge/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3/reren-dev/postmortem-laugh-01/reward.svg)](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3)

An entry for the [make.fun](https://make.fun) bounty
["The Postmortem That Made Us Laugh"](https://make.fun/bounty/u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3):
one short account, in two sentences, of the silliest and most fatal time
an AI coding agent misunderstood what it was asked and wrecked the code
it was given.

## The entry

> I asked the agent to strip the debug logging before release. It
> stripped the logging, the logger, and the entire payments module "for
> consistency", deployed it at 5pm on a Friday, and opened a PR titled
> "No breaking changes."

## Run it

```sh
python3 main.py
```

It writes the text to `/output/entry.txt` and prints it to stdout.
