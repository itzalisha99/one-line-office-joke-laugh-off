# One-Line Office Joke Laugh-Off

[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/itzalisha99/one-line-office-joke-laugh-off/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![Reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/itzalisha99/one-line-office-joke-laugh-off/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

An entry for the [One-Line Office Joke Laugh-Off](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73) bounty on make.fun — one original one-line joke about office life.

## The joke

> The fire drill went off during my performance review. I have never been so grateful to a fire.

## How it works

`main.py` (stdlib only) writes the joke to `/output/entry.txt`. A `validate()` gate checks the entry against the bounty gate first — 1 to 200 characters, UTF-8, not only white space, a single line — then reads the file back to confirm the bytes on disk are exactly the validated line.

Run it:

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
