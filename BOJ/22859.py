import re

html = input()

tagStack = []
offset = -1
while offset < len(html) - 1:
    offset += 1

    if html[offset] == "<":
        # TAG PARSING
        tagName = ""
        tagTitleAttr = ""
        tagClose = False

        offset += 1
        while html[offset] != ">":
            if html[offset] != "/":
                tagName += html[offset]
            else:
                tagClose = True
            offset += 1
        
        if "div" in tagName:
            # Process for <div> tag

            titleAttrRegex = re.compile(r'.+\s+title="(.+)"')

            if titleAttrRegex.match(tagName):
                tagTitleAttr = titleAttrRegex.match(tagName).group(1)

                if tagTitleAttr: print("title :", tagTitleAttr)
        elif tagName == "p":
            # Process for <p> tag

            innerHtml = ""

            offset += 1
            while html[offset - 3:offset + 1] != "</p>":
                innerHtml += html[offset]
                offset += 1

            # Remove all of inner tags / strip leftmost & rightmost whitespaces / remove duplicated whitespaces
            print(re.sub(r" +", " ", re.sub(r"<\/?[a-z]+\s?>", "", innerHtml[:-3]).strip()))
        else:
            # Process for other tags
            # (Not necessary part)

            if not tagClose:
                tagStack.append(tagName)
            else:
                last = tagStack.pop()