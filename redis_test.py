import redis
r = redis.Redis(host='redis-19817.c17.us-east-1-4.ec2.cloud.redislabs.com', port='19817', 
                password='nC6WdDnB2YPe4VVEUfHmIY5JCmESFgir')
r.set('hello', 'world')
print(r.get('hello'))

