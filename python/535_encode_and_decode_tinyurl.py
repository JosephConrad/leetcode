import random
import string


class Codec1:
    def __init__(self):
        self.urls = []

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        self.urls.append(longUrl)
        return "http://tinyurl.com/" + str(len(self.urls) - 1)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.urls[int(shortUrl.split("/")[-1])]


class Codec:
    alphabet = string.ascii_letters + '0123456789'

    def __init__(self):
        self.url2code = {}
        self.code2url = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        while longUrl not in self.url2code:
            code = ''.join([random.choice(Codec.alphabet) for _ in range(6)])
            if code not in self.code2url:
                self.url2code[longUrl] = code
                self.code2url[code] = longUrl
        return "http://tinyurl.com/" + self.url2code[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.code2url[shortUrl[-6:]]


if __name__ == "__main__":
    # Your Codec object will be instantiated and called as such:
    codec = Codec()
    print codec.encode("https://leetcode.com/problems/design-tinyurl")
    print codec.encode("https://leetcode.com/problems/design-tinyurl")
    print codec.decode(codec.encode("https://leetcode.com/problems/design-tinyurl"))
