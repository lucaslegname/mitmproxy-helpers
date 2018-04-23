# Redirect

This script allows you to create rules to change requests host "on-the-fly". You can use the `host_filter` to limit redirection to a single host. You can also add as many redirection rules as you need in the `redirect_rules` array.

## How to use script
Start mitmproxy using the following command :
```
mitmproxy -s redirect.py
```
