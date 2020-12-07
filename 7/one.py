with open('input.txt') as f:
    rules = f.read().splitlines()

colors = list(map(lambda rule: rule.split(' bags')[0], rules))

bag_key = {}

# exracting info
for rule in rules:

    # get color of bag that is being described
    color = rule.split(' bags')[0]

    # split bag contents
    bag_content = rule.split('contain ')[1].replace('.', '').split(', ')

    # filter out bags without any content
    bag_content = list(filter(lambda content: content != 'no other bags', bag_content))

    # get the count of each bag in content
    counts = list(map(lambda content: int(content.split()[0]), bag_content))

    # get rid of count and the word "bag" from bag content
    bag_content = list(map(lambda content: ' '.join(content.split()[1:]).replace('bags', '').replace('bag', '').strip(), bag_content))

    # pair bag content with count
    paired = list(zip(bag_content, counts))

    # turn them into a dictionary
    paired = list(map(lambda pair: {'color': pair[0], 'count': pair[1]}, paired))

    # add it to dictionary
    bag_key[color] = paired


# recursively check each bag for any shiny gold bags
def search_for_gold(bag_color):
    
    content = bag_key[bag_color]
    
    for bag in content:
        color, count = bag.values()

        if color == 'shiny gold':
            return True

        if search_for_gold(color):
            return True

    return False
        


has_gold = 0

# go through each bag in all bags
for color, content in bag_key.items():

    if search_for_gold(color):
        has_gold += 1

print(has_gold)

