""" dynamically load settings

author baiyu
"""
import conf.global_settings as settings

## coding tips: load config settings to Class dynamically
class Settings:
    def __init__(self, settings):

        for attr in dir(settings):
            ## build-in variable or build-in function is lowercase, so the settings in config file are uppercase which are coded by author.
            if attr.isupper():
                setattr(self, attr, getattr(settings, attr))

settings = Settings(settings)