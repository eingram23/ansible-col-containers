vault policy write secrets - <<EOF
path "secret/*" {
  capabilities = [ "read" ]
}
EOF