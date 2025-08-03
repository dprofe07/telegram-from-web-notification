#!/usr/bin/python3
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("id", help="You ID, given by tg bot")
parser.add_argument("message", help="Message to send")
parser.add_argument("--hostname", help="Host where application is hosted", default="dprofe.ddns.net")

args = parser.parse_args()

requests.post(
    f'https://{args.hostname}/tg-notify/',
    {
        'id': args.id,
        'message': args.message
    }
)
print('Message sent')


