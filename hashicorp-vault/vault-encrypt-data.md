
- Encrypt creditcard number. keyring is credit card, path is encryption, transit secret engine is mounted at 'encryption' path. The pain text must be encoded to base64, otherwise it will show error. 
```
vault write encryption/encrypt/creditcard plaintext=$(base64 <<< "1234 5678 9021 1763") 
```
