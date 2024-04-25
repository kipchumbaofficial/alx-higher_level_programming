#!/bin/bash
# Curl body size

curl -s -w "%{size_download}\n" $1
