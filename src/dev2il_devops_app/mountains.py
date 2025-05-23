def highest_mountain(mountains):
    """
    Returns the highest mountain from a list of mountains.
    
    :param mountains: List of mountains, where each mountain is a dictionary with 'name' and 'height'.
    :return: The mountain with the highest height.
    """
    if not mountains:
        return None
    return max(mountains, key=lambda x: x['height'])