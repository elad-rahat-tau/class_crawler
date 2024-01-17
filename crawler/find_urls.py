import urllib.request
import html.parser
import urllib.parse
import html.parser
try:
    import crawler.links
except:
    import links





class FindUrls:
    def __call__(self, url):
        response = urllib.request.urlopen(url)
        html = response.read().decode('utf-8')

        try:
            a = crawler.links.Links(html)
        except:
            a = links.Links(html)
        html_links = a._links
        html_links_list = list(html_links)
        for i in range(len(html_links_list)):
            html_links_list[i] = urllib.parse.urljoin(url, html_links_list[i])
        html_links = set(html_links_list)

        return(html_links)





