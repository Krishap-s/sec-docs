#p(a)wnshop

Author: [Krishap-s](https://github.com/Krishap-s)

## Brief Description:

- Web challenge solved by urlencoding , email verification bypass and blind elastic search injection

## Requirements:

- Knowledge of flask, nginx, apache cgi bins, elastic search

## Source:

- [Source Code]("assets/pawnshop-a5a3b06ddfb3bbd8002b55ba65794d89.zip")
- [Exploit]("assets/exploit.py")
- [ElasticSearch query docs]("https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html")
- [Blind SQL injection]("https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjXncSn3M7wAhVuxzgGHeYbD_UQFjABegQIAhAD&url=https%3A%2F%2Fportswigger.net%2Fweb-security%2Fsql-injection%2Fblind&usg=AOvVaw2LTHWkA9pQsL-Bc05-W5lb")

## Exploitation:

- Through the source code and Docker-compose file we can determine there are two servers running nginx and apache

- The apache server is responsible for running backend tasks using python cgi-bins (basically php but with other languages) 

- The nginx server acts as a reverse proxy (middle man between client and server) while also serving static files


###Architecture:
```
 
Apache -->   Nginx   --> client
		^
		|
		|
	   Static files

```

- The apache server has two executable python file 'index.py' and 'admin.py'

- If the url contains "/backend/$1" nginx forwards request to apache "http://apache.server/$1"

- The index.py can be accessed normally but the admin.py is being protected by a basic auth authentication set up in the nginx config

- The nginx uses a regex find for the term 'admin' in the url path, if it is true it requests authentication from the user

### URL regex bypass:

1) We url encode the first character of the "admin.py" to "%61dmin.py"

2) We again url encode the first three characters of the url encoded string "%25%36%31dmin.py"

3) Then we send the request to url "https://$url/backend/%25%36%31dmin.py"

What happens is:
```
%25%36%31dmin.py --> %61dmin.py --> admin.py

		     Decoded by    Decoded by
    Client             Nginx         Apache
                  (doesn't trigger (Apache runs
                     regex)         admin.py)
```
Now, we can run admin functions

- The admin.py contain a lookup function and a list function which can be run by using a post request with either "action=lookup" and "action=list" respectively

- The lookup function takes a mail parameter from the post request and runs email verification against it and finally a lookup function
### Email verification bypass:

1) In the funcs.py in the apache src, the email verification runs an email.utils.parseaddr and then checks if the parsed address:
  - Is'nt empty
  - Matches the original string
  - Had '@' and a '.' at the end

### Blind Elasticsearch injection:

1) The lookup function runs a query for items with the seller email same as the one we enter 
2) Since the query was made with a string concatenation we can perform an injection here with the mail variable
3) Since the lookup function doesn't return any of the response data to us we have to rely on found and not found messages to extract data 

- The method is similar to Blind sql injection

After the email verification bypass and ElasticSearch injection we use payload
```" AND (value:'$input' AND id:5) OR seller:"jmffc@pawnshop.2021.3k.ctf.to ```

- Elastic search uses ? for wildcard operator, this can be used to determine the number by constantly increasing '?' operator in the input until a found message is recieved

Finally we find flag to be 39 characters

- By Bruteforcing a character position with all ascii characters we can find the character at that position.Do the same for all 39 characters

Finally we get the flag

##Flag:

3k{http2_4nd_email_val1dation_y0u_s41d_huh}
  
