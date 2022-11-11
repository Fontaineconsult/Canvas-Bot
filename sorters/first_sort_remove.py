

from config.read import read_config
items_to_remove = read_config()['sorters']



def first_sort_remove(links) -> list:

    first_pass = [link for link in links if link not in items_to_remove['first-sort-remove']]

    second_pass  = [link for link in links if not items_to_remove['first-sort-remove-regexs']]


