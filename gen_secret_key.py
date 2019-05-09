"""
Utility file to print & generate a secret key.

This file is to be run when running a docker build, so that a secret key is generated & stored for seedme2's django app to use.
"""
import random
import string

print("".join(
    [random.SystemRandom().choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)]))
