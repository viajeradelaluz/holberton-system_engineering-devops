# 0x1B. Web stack debugging #4

## Resources

- [
Nginx failed: 24: Too many open files](https://www.claudiokuenzler.com/blog/850/nginx-socket-failed-24-too-many-open-files)


## Tasks

### **0. Sky is the limit, let's bring that limit higher**

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests.

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

```bash
root@2cdcf307589d:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   3.405 seconds
Complete requests:      2000
Failed requests:        343
   (Connect: 0, Receive: 0, Length: 343, Exceptions: 0)
Non-2xx responses:      1657
Total transferred:      907326 bytes
HTML transferred:       542973 bytes
Requests per second:    587.39 [#/sec] (mean)
Time per request:       170.245 [ms] (mean)
Time per request:       1.702 [ms] (mean, across all concurrent requests)
Transfer rate:          260.23 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    4  15.7      0      98
Processing:     5  160  47.0    190     290
Waiting:        5  154  47.1    188     208
Total:         12  163  48.0    191     294

Percentage of the requests served within a certain time (ms)
  50%    191
  66%    196
  75%    198
  80%    199
  90%    202
  95%    204
  98%    207
  99%    283
 100%    294 (longest request)
```

Output once the script is executed:

```bash
root@2cdcf307589d:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   3.387 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    590.56 [#/sec] (mean)
Time per request:       169.331 [ms] (mean)
Time per request:       1.693 [ms] (mean, across all concurrent requests)
Transfer rate:          491.94 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   34  45.3      4     189
Processing:     1  135 116.3    101     701
Waiting:        1  113 112.0    100     605
Total:          2  168 125.9    189     800

Percentage of the requests served within a certain time (ms)
  50%    189
  66%    196
  75%    198
  80%    199
  90%    206
  95%    297
  98%    690
  99%    800
 100%    800 (longest request)
```
