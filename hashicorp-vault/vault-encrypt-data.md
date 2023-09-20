
- Encrypt creditcard number. keyring is credit card, path is encryption, transit secret engine is mounted at 'encryption' path. The pain text must be encoded to base64, otherwise it will show error. 
```

vault write encryption/encrypt/creditcard plaintext=$(base64 <<< "1234 5678 9101 1121") 
Key        Value 
---        ----- 
ciphertext vault:v3:cZNHVx+sxdMErXRSuDa1q/pz49fXTn1PScKfhf+PIZPvy8xKfkytpwKcbC0fF2U=
```
