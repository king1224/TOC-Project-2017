# TOC Project 2017

Implement Code for TOC Project 2017

A telegram bot based on a finite state machine

## Setup

### Prerequisite
* Python 3

#### Install Dependency
```sh
pip install -r requirements.txt
```

* pygraphviz (For visualizing Finite State Machine)
    * [Setup pygraphviz on Ubuntu](http://www.jianshu.com/p/a3da7ecc5303)

### Secret Data

`API_TOKEN` and `WEBHOOK_URL` in app.py **MUST** be set to proper values.
Otherwise, you might not be able to run your code.

### Run Locally
You can either setup https server or using `ngrok` as a proxy.

**`ngrok` would be used in the following instruction**

```sh
ngrok http 5000
```

After that, `ngrok` would generate a https URL.

You should set `WEBHOOK_URL` (in app.py) to `your-https-URL/hook`.

#### Run the sever

```sh
python3 app.py
```

## Finite State Machine
![fsm](./img/show-fsm.png)

## Usage
This bot is design to help frauds. The bot will try to let you pay the bills with text certification whatever you said.

The initial state is set to `wait`.
Wait to start with a message: `/start`. Can be stopped at any time with a message: `/stop`

After start the bot, there will nine situations. The bot will point you what you should say in specific situation. Once you found that the bot is cheating you, you can send a message `fuck you` to interrupt the situation.

* user
	* Input: "Hi"
		* In to concern state
		* The bot will pretend he is your classmate

	* Input: "Joke"
		* In to joke state
		* The bot will give you random joke

	* Input: "I wanna be loved"
		* In to love state
		* The bot will give you random joke

	* Input: "insult me"
		* In to insult state
		* The bot will make fun with you

	* Input: "My life is no color"
		* In to suicide state
		* Here is a suicide prevention service, you can get some information here.

	* Input: "Someone told me he kidnapped my son"
		* In to cheatprevention state
		* Here is a fraud prevention service, you can get some information here.

	* Input: "capoo"
		* In to capoo state
		* The bot will show you `capoo` with photo

	* Input: "Tzu-Yu"
		* In to tzuyu state
		* The bot will show you `Tzu-Yu` with video

	* Input: "TT"
		* In to tt state
		* The bot will show you `TT` with audio


## Reference
[Lee-W](https://github.com/Lee-W)
