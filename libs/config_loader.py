# encoding: utf-8

import yaml

class ConfigLoader(object):
    base_dir = None
    env = None
    cache = {}

    def __init__(self):
        pass

    def setup(self, base_dir, env):
        self.base_dir = base_dir # configs/
        self.env = env # prod

    def get(self, conf_name):
        if not self.cache.get(conf_name):
            file_name = self.base_dir + self.env + "/" + conf_name + ".yaml"
            self.cache[conf_name] = yaml.load(open(file_name))
        return self.cache.get(conf_name)

config = ConfigLoader()
