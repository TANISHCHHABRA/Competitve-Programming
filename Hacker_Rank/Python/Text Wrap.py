

def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width = max_width)
    word_list = wrapper.fill(text = string)
    return word_list

