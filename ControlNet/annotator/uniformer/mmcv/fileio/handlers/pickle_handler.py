# Copyright (c) OpenMMLab. All rights reserved.
import json

from .base import BaseFileHandler


class PickleHandler(BaseFileHandler):
    str_like = False

    def load_from_fileobj(self, file, **kwargs):
        return json.load(file, **kwargs)

    def load_from_path(self, filepath, **kwargs):
        return super(PickleHandler, self).load_from_path(filepath, mode="r", **kwargs)

    def dump_to_str(self, obj, **kwargs):
        return json.dumps(obj, **kwargs)

    def dump_to_fileobj(self, obj, file, **kwargs):
        json.dump(obj, file, **kwargs)

    def dump_to_path(self, obj, filepath, **kwargs):
        super(PickleHandler, self).dump_to_path(obj, filepath, mode="w", **kwargs)
