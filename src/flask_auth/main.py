from providers import VK_Service_Provider


class FlaskAuthentication:
    def __init__(self, active_providers: list) -> None:
        self.active_providers = active_providers
        if "vk" in active_providers:
            self.vk_service = VK_Service_Provider("vk", "https://oauth.vk.com/authorize", {"client_id": "********", "redirect_uri":"domain_name", "scope": "pages"}, False)
            #print(self.vk_service.get_authorization_url)
        


               
                    
if __name__ == "__main__":
    main_class = FlaskAuthentication(["vk"])
    
