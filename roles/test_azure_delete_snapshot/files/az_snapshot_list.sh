#!/bin/sh

az snapshot list --query "[?tags.Expiry != values[]]" -o json > "{ item }"
