# EDOPro whitelist maker

A python script that generates banlists in form of whitelists using the [yugioh banlists api](https://github.com/karim-xyz/yugioh-banlists-api) and the [ygoprodeck api](https://ygoprodeck.com/api-guide/)

What whitelists do is simply limiting the "card pool" to only the ones you specified in the file, for example the official [GOAT whitelist](https://github.com/ProjectIgnis/LFLists/blob/master/GOAT.lflist.conf)

---

## Setup and Usage

install dependencies
```
pip install -r requirements.txt
```

then run the main.py file and give it the banlist date in yyyy-mm format

```
python3 main.py
banlist date [yyyy-mm]: 2002-05
Done
```
And [this file](2002.5.lflist.conf) is created


