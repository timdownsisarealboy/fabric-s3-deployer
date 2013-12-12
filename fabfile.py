from fabric.api import *
from boto.s3.connection import S3Connection
import os
from boto.s3.key import Key

ignores = [".git"]

def deploy(key, secret, domain, folder):
    conn = S3Connection(key, secret)
    domain_arr = [domain, "www." + domain]

    for d in domain_arr:
        b = conn.get_bucket(d)
        print b
        for dirname, dirnames, filenames in os.walk(folder):
            for ignore in ignores:
                if(ignore in dirnames):
                    dirnames.remove(ignore)
            for filename in filenames:
                    k = Key(b)
                    k.key = filename
                    k.set_contents_from_filename(folder + "/" + filename)
                    k.make_public()
                    print filename
