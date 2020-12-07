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



total_bags = 0
# recursively check each bag for any shiny gold bags
def search_bag(bag_color):
    global total_bags
    
    content = bag_key[bag_color]
    print(bag_color, content)

    total_bags += 1
    print(total_bags)
    
    for bag in content:

        color, count = bag.values()

        for _ in range(count):
            search_bag(color)
        

search_bag('shiny gold')

print(total_bags-1)

