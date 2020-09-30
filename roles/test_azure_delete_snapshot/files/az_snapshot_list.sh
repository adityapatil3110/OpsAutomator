#!/bin/sh

Filename= "{item}"

az snapshot list --query "[?tags.Expiry != values[]]" -o json > ${ Filename }
