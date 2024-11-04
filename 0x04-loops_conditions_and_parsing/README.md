# SSH RSA Key Pair Creation

This project involves the creation of an SSH RSA key pair that will be used for secure access to remote servers. The key pair consists of a public key, which will be shared, and a private key, which should be kept secure.

## Key Steps

1. **Generating RSA Key Pair:**
   - An RSA key pair was generated using the `ssh-keygen` command.
   - The public key is stored in `0-RSA_public_key.pub`.
   - The private key is saved securely in the default location (`~/.ssh/id_rsa`).

2. **Public Key:**
   - The public key can be found in the `0-RSA_public_key.pub` file.
   - This public key should be added to the SSH public key field of your intranet profile for server access.

3. **Private Key Security:**
   - The private key (`~/.ssh/id_rsa`) should not be shared and must be stored in a secure location, such as a password manager or USB key.

4. **Bash Script:**
   - Any necessary Bash scripts created for this project follow the specified format:
     - Each script starts with `#!/usr/bin/env bash`.
     - A comment is included to explain what the script does.
   - All scripts have been made executable and have been checked for compliance using Shellcheck.

## Shellcheck Verification

All Bash scripts in this project have been checked using Shellcheck (version 0.7.0) and pass without any errors. This ensures that the scripts adhere to best practices and avoid common pitfalls.

## Conclusion

This setup is essential for securely managing access to servers, ensuring that only authorized users can connect via SSH.

