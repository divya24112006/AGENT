import os
import re
import urllib.parse

CLIENT_EMAIL = os.getenv("CLIENT_EMAIL","")

KEYWORDS =(
  "gmail", "email", "mail",
  "write an email", "send an email", "draft an email",
  "compose an email", "write an email", "send mail", "draft mail",
  "compose mail"
)

def is_email_command(text):
  text = text.lower()
  return any(k in text for k in KEYWORDS)
