# -*- coding: utf-8 -*-

from benedict.utils import type_util


def _merge_dict(d, other):
    for key, value in other.items():
        _merge_item(d, key, value)


def _merge_item(d, key, value):
    item = d.get(key, None)
    if type_util.is_dict(item) and type_util.is_dict(value):
        _merge_dict(item, value)
    else:
        d[key] = value


def merge(d, other, *args):
    others = [other] + list(args)
    for other in others:
        _merge_dict(d, other)
    return d
