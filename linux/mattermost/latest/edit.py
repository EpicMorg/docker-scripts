#!/usr/bin/python2
import os
fp = open(os.path.join(os.path.dirname(__file__), "mattermost"), "r+b")
print("Try before buy (c)")
try:
    pos = fp.read().find("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyZmShlU8Z8HdG0IWSZ8r\ntSyzyxrXkJjsFUf0Ke7bm/TLtIggRdqOcUF3XEWqQk5RGD5vuq7Rlg1zZqMEBk8N\nEZeRhkxyaZW8pLjxwuBUOnXfJew31+gsTNdKZzRjrvPumKr3EtkleuoxNdoatu4E\nHrKmR/4Yi71EqAvkhk7ZjQFuF0osSWJMEEGGCSUYQnTEqUzcZSh1BhVpkIkeu8Kk\n1wCtptODixvEujgqVe+SrE3UlZjBmPjC/CL+3cYmufpSNgcEJm2mwsdaXp2OPpfn\na0v85XL6i9ote2P+fLZ3wX9EoioHzgdgB7arOxY50QRJO7OyCqpKFKv6lRWTXuSt\nhwIDAQAB")
    fp.seek(pos)
    fp.write("MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmCvX08GJRrbqYZbJtGXj\nXYmoRva8Yvk43uspBiNQoFYp0N8mWfmDhCqUzW7i9GZKDlEgn2IYoL2GxiRpSJaP\nirK8FGwD+o0efzhTHeGWOvD4e0c8gQZbpe85p17vha2i2xZiWQ4UBlq7jUFcuy6F\nfcgUK+fVI8+IvvjtkIZRqRLLlXCRnpuEWq/8vJF7yHql2jxiGUdXkFkZsgPgXizv\nmY0op5ui6n/f7ljVIIdad10OLNsW/xxk6VxirAIyuDZK9GSRGjjvDhi/yNcC0yJe\njYTCeDoD+GVh3twk+RyFo9S1AG7kKWtHTNu3MLh9/XnRJdpgrlAE7Z4+VfHrsbXp\ntwIDAQAB")
    print("OK")
except:
    print("Nothing to do")
finally:
    fp.close()
