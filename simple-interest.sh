#!/bin/bash

# Simple Interest Calculator

read -p "Enter the principal amount: " p
read -p "Enter the annual rate of interest (%): " r
read -p "Enter the time period (years): " t

si=$(awk "BEGIN {printf \"%.2f\", ($p * $r * $t) / 100}")

echo "Simple Interest: $si"
