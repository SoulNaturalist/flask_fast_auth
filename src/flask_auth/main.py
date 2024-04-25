from providers import VK_Service_Provider


class FlaskAuthentication(object):
    def __init__(self, active_providers: list, app=None) -> None:
        self.active_providers = active_providers
        if app is not None:
            self.app = app
            self.init_app(self.app)
        else:
            self.app = None
        
    def init_app(self, app):
        pass
        #some configuration app extension

               
                    
if __name__ == "__main__":
    main_class = FlaskAuthentication(["vk"])
    
