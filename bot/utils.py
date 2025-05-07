def get_tag_value(tags, key):
    for tag in tags:
        if tag.get('Key') == key:
            return tag.get('Value')    
    return 'N/A'
