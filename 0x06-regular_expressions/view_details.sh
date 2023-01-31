#!/usr/bin/env bash
while read -r line; do ./100-textme.rb "$line" | cat -e; sleep 1s; done < text_messages.log
