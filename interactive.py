#!/usr/bin/env python3
import random, string, argparse
parser = argparse.ArgumentParser()
parser.add_argument("passwordLength", type=int,
                    help="How much character long?")
args = parser.parse_args()
print (''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(args.passwordLength)))
