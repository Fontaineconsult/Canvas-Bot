

from config.read import read_config
from sorters.sorter_re import re_combiner

items_to_remove = read_config()['sorters']



def links_to_remove(links) -> list:

    first_pass = [link for link in links if link not in items_to_remove['first-sort-remove']]

    regex = re_combiner(items_to_remove['first-sort-remove-regexs'])

    second_pass  = [link for link in first_pass if not regex.match(link)]


    return second_pass




print(re_combiner(items_to_remove['first-sort-remove-regexs']))