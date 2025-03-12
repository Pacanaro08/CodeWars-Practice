# You have a collection of lovely poems. Unfortunately, they aren't formatted very well. They're all on one line, like this:
# Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
# What you want is to present each sentence on a new line, so that it looks like this:
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.

def format_poem(poem):
    return '.\n'.join(poem.split('. '))