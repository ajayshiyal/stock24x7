# custom_filters.py
from django import template
import pandas as pd
register = template.Library()
import json  

@register.filter(name='dict_key')
def dict_key(d, key):
    return d.get(key, '')




@register.filter
def replace_nan(value):
    if pd.isna(value) or value == 'N/A':
        return 'Data not available'
    return value


@register.filter
def to_json(value):
    """
    Convert Python object to JSON string and escape special characters for use in JavaScript.
    """
    return json.dumps(value)