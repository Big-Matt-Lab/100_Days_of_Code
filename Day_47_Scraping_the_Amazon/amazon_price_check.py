import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS/ref=sr_1_1?crid=2NHCVHO6T7BDD&dib=eyJ2IjoiMSJ9.F0tgUSn3kGSDJE6qv-yiYWy9PGDzeFJYr6t7GpjxKLQBm8sTBXAM3A9juJG_0OABzS9NG6rYaEx3q0JRhstzm4R2qySLJFlZYdo4aFHIsu4p5hDVonZr6sWnb9q9aoBFkRPs5bhfH9akuWGltn6PrnzdjlOtI9t7NqGlns2d7bgwib1g-RKuY1wP2lHXdwhxjNv2RDZFnVcyHawepnwAgZCaUiNXc7yWR_YtAW7W1S4.5T6NH79NZ0hCTSMb06TExfVi_RULwy3LZRPK2dbvjJ8&dib_tag=se&keywords=instant%2Bpot&qid=1787078791&sprefix=isntant%2Bpot%2Caps%2C239&sr=8-1&th=1"
response = requests.get(URL, timeout=5)
response.raise_for_status()
data = response.text

# Make soup
soup = BeautifulSoup(data, "html.parser")
price = soup.find(name="div", id="nav-logo")
banners = [div.find("a") for div in price]
print(banners)
article_texts = [banner.getText() for banner in banners]
article_links = [banner.get("href") for banner in banners]
print(article_links)
# price_split = price.split('.')
# price_int = int(price_split[0])
# print(price_int)
# if price_int < 100:
#     pass
#
# #
