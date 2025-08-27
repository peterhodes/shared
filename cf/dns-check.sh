#!/usr/bin/env bash
set -euo pipefail

# Domain to query
DOMAIN="voice-commerce.com"

# Record types to query
RECORDTYPES="A AAAA CNAME MX TXT SPF NS SOA \
SRV CAA NAPTR PTR \
DNSKEY DS RRSIG NSEC NSEC3 NSEC3PARAM \
SVCB HTTPS"

# Find authoritative nameservers for the domain
DNS_SERVERS="$(dig "$DOMAIN" NS +short | sed 's/\.$//')"

echo "==> Authoritative nameservers for $DOMAIN:"
printf ' - %s\n' $DNS_SERVERS
echo

# Loop through each authoritative nameserver
for ns in $DNS_SERVERS; do
  echo "===== Queries to $ns ====="
  
  # Loop through all record types
  for r in $RECORDTYPES; do
    echo "--- $r ---"
    dig "$DOMAIN" "$r" @"$ns" +nocmd +noall +answer || true
  done
  
  # Explicitly check DMARC
  echo "--- DMARC TXT (_dmarc.$DOMAIN) ---"
  dig "_dmarc.$DOMAIN" TXT @"$ns" +nocmd +noall +answer || true
  echo
done
