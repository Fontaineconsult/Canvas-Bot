import requests, os, network.selenium_scraper, json
from urllib.parse import urlparse, urlunparse


def get_module_item(course_id, module_id, item_id):
    api_url = f"https://sfsu.instructure.com/api/v1/courses/{course_id}/modules/{module_id}/items/{item_id}?access_token={os.environ.get('access_token')}"
    item_get = requests.get(api_url)
    if item_get.ok:
        item_content = json.loads(item_get.content)
        if item_content.get("url"):
            print(item_content)
            parsed = urlparse(item_content['url'])
            remove_api_path = parsed.path.split("/")[3:]
            return_url = urlunparse((parsed.scheme, parsed.netloc, "/".join(remove_api_path), parsed.params, parsed.query, parsed.fragment))
            return return_url
        if item_content.get("external_url"):
            return item_content.get("external_url")


    else:
        print("API DIDN'T WORK")



