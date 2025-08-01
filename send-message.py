import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("id", help="You ID, given by tg bot")
parser.add_argument("message", help="Message to send")

args = parser.parse_args()

requests.post(
    'https://dprofe.ddns.net/tg-notify/',
    {
        'id': args.id,
        'message': args.message
    }
)
print('Message sent')


