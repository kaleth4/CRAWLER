import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
import sys

class WebCrawler:
    def __init__(self, base_url, max_depth=3, headers=None, cookies=None):
        self.base_url = base_url
        self.max_depth = max_depth
        self.visited = set()
        self.headers = headers if headers else {}
        self.cookies = cookies if cookies else {}
        self.domain = urlparse(base_url).netloc

    def is_in_scope(self, url):
        return urlparse(url).netloc == self.domain

    def crawl(self, url, depth=0):
        if depth > self.max_depth or url in self.visited:
            return

        self.visited.add(url)
        print(f"[+] Crawling ({depth}): {url}")

        try:
            response = requests.get(
                url,
                headers=self.headers,
                cookies=self.cookies,
                timeout=10,
                verify=False
            )
        except requests.RequestException as e:
            print(f"[-] Error al acceder: {e}")
            return

        self.analyze_response(url, response)

        soup = BeautifulSoup(response.text, "html.parser")

        for link in soup.find_all("a", href=True):
            next_url = urljoin(url, link["href"])
            next_url = next_url.split("#")[0]

            if self.is_in_scope(next_url):
                self.crawl(next_url, depth + 1)

    def analyze_response(self, url, response):
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if params:
            print("    [*] Parámetros detectados:")
            for param in params:
                print(f"        - {param}")

        soup = BeautifulSoup(response.text, "html.parser")
        forms = soup.find_all("form")

        for form in forms:
            action = form.get("action")
            method = form.get("method", "get").lower()
            print("    [*] Formulario encontrado:")
            print(f"        - Acción: {action}")
            print(f"        - Método: {method}")

            for input_tag in form.find_all("input"):
                name = input_tag.get("name")
                input_type = input_tag.get("type", "text")
                if name:
                    print(f"            - Input: {name} ({input_type})")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python crawler.py https://intel.arkm.com/")
        sys.exit(1)

    target = sys.argv[1]

    headers = {
        "User-Agent": "OpenBash-WebCrawler/1.0"
    }

    crawler = WebCrawler(
        base_url=target,
        max_depth=3,
        headers=headers
    )

    crawler.crawl(target)
