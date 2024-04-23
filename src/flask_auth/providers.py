import requests

class Provider:
    def __init__(self, name, url, app_meta_data, open_id) -> None:
        self.name = name
        self.url = url
        self.app_meta_data = app_meta_data
        self.open_id = open_id

    @property
    def get_authorization_url(self):
        if self.name == "vk" and self.app_meta_data and self.app_meta_data.get("redirect_uri") and self.app_meta_data.get("client_id"):
            return "https://oauth.vk.com/authorize?client_id={}&redirect_uri={}&scope={}&response_type=token".format(
                self.app_meta_data["client_id"], self.app_meta_data["redirect_uri"], self.app_meta_data["scope"]
            )

    def data_handler(self):
        raise NotImplementedError("Subclasses must implement data_handler method")


class VK_Service_Provider(Provider):
    def data_handler(self, token):
        try:
            return requests.get(
                "https://api.vk.com/method/account.getProfileInfo?v=5.132&access_token={}".format(token)
            ).json()["response"]
        except KeyError:
            return None


class Google_Service_Provider(Provider):
    pass


class Github_Service_Provider(Provider):
    pass