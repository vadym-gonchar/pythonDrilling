import textwrap

def wrap(string, max_width):
    #variant 1)
    return textwrap.fill(string, max_width)

    #variant 2)
    # wrapper = textwrap.wrap(string, max_width)
    # return '\n'.join(wrapper)

    #variant 3)
    # wrapper = textwrap.TextWrapper(width=max_width)
    # wrapped_lines = wrapper.wrap(string)
    # wrapped_paragraph = "\n".join(wrapped_lines)
    # return wrapped_paragraph

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
