# CassieApi

A simple API written in Python.  
Designed for a chatbot / virtual assistant. 

https://stats.uptimerobot.com/YxNP5UDOLV <= API should be up and running.


## Chatbot

Uses the `neuralintents` library, which uses tensorflow and nltk to make an AI chatbot. 

## Installation

Clone the repository: `git clone https://github.com/saberswordboy/cassieapi`  

Configure the settings in `config/config.ini`: Change 'ip' and 'server_ip' to your server's IP address, or localhost for testing.  

Install the requirements: `pip3 install -r requirements.txt` This may take a while, NeuralIntents is quite large with Tensorflow.  

Run the server: `python3 server.py`

Open a new shell and start the client! `python3 client.py`
