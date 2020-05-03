# Multicore Request
MulticoreRequest module wraps up multiprocessing and requests module together to speed up rest calls made in bulk.

# Usage
```python
from MulticoreRequest import MulticoreRequest

# data input for making calls
call_pack = [
    {'url': 'http://google.com', 'type':'get'},
    {'url': 'http://someserver.com', 'type': 'post', 'data': '{'key': 'value'}'}
]

# number of processes, default = 10
procs = 50

mc_req = MulticoreRequest(call_pack=call_pack, procs=procs)
mc_req.make_call()
```

# Feature List
- [X] GET calls
- [X] Post calls
- [X] Post and Get calls in synchronously
- [ ] Post request additional arguments
- [ ] Support for PUT, PATCH, UPDATE
- [ ] Some nice to have stuff!
