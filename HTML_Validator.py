#!/bin/python3


def validate_html(html):
	string = _extract_tags(html)
	s = []
	balanced = TRUE
	for tag in string:
		if "/" not in tag:
			s.append(tag)
		else:
			if s == []:
				balanced = FALSE
			else:
				top = s.pop()
				if top[1:] != tag[2:]:
					return FALSE
	if balanced = TRUE and s == []:
		return TRUE
	else:
		return FALSE
    '''
    This function performs a limited version of html validation by checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm from the book
    # the main difference between your code and the book's code will be that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags


def get_first_tag(html):
    start = html.index('<')
    end = html.index('>')+1
    tag = html[start:end]
    return tag


def _extract_tags(html):
    if '<' not in html:
        return []
    else:
        return [get_first_tag(html)]+get_tags(html[html.index('>')+1:])
    
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
