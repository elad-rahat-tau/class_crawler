import pytest
import subprocess
import crawl
import find_urls
import yaml

def get_yaml(file_server, depth=100):

    links_yaml = open("C:/users/user/desktop/links.yaml","w")

    url_crawls = crawl.Crawl(file_server, depth, find_urls=find_urls.FindUrls())
    url_crawls_list = url_crawls.web_of_links()

    for i in range(len(url_crawls_list)):
        yaml.dump({"level": i, "links": url_crawls_list[i]}, links_yaml)
