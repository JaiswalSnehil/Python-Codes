import secrets

c = 6
otp = ''.join(str(secrets.randbelow(10))
              for _ in range(c))

print('Generated OTP:', otp)