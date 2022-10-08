# Cipher

Encryption program that uses a one-time pad (OTP) cipher, which uses a different shift for every letter in the message.

To implement the cipher, the sender of a message generates a random sequence of characters, the pad, where each character in the pad is an uppercase letter. Each of these letters indicates how much each letter in the message itself should be shifted by in order to encrypt it. In order to decipher the message, the receiver uses the pad to unshift each letter by the specified amount. The pad is then discarded, hence "one-time" pad.

This pad cannot be cracked if the pad is random, the pad is longer than the message being encrypted, the pad is only known to the sender and receiver, and it is only used once.
