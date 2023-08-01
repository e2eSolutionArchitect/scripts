
- Encrypt creditcard number. keyring is creditcard, path is encryption, transit secret engine is mounted at 'entryption' path. 
```
vault write encryption/encrypt/creditcard plaintext=$(base64 <<< "1234 5678 9021 1763") 
```
