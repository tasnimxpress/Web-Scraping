# important html tag

tag_dict = [
    {'head':
        'The <head> element is a container for metadata (data about data) and is placed between the <html> tag and the <body> tag'},

    {'body': "The <body> tag defines the document's body.\nThe <body> element contains all the contents of an HTML document, such as headings, paragraphs, images, hyperlinks, tables, lists, etc.\nNote: There can only be one <body> element in an HTML document."},

    {'header':
        "The <header> element represents a container for introductory content or a set of navigational links.\nA <header> element typically contains:\none or more heading elements (<h1> - <h6>)\nlogo or icon\nauthorship information"},

    {'article': "The <article> tag specifies independent, self-contained content.\nPotential sources for the <article> element:\nForum post\nBlog post\nNews story"},

    {'p': "The <p> tag defines a paragraph."},

    {'div': "The <div> tag defines a division or a section in an HTML document.\nThe <div> tag is used as a container for HTML elements - which is then styled with CSS or manipulated with JavaScript.\nThe <div> tag is easily styled by using the class or id attribute.\nAny sort of content can be put inside the <div> tag! "},

    {'<h1>-<h6>': "The <h1> to <h6> tags are used to define HTML headings.\n<h1> defines the most important heading. <h6> defines the least important heading."},

    {'nav': "The <nav> tag defines a set of navigation links.\nNote that NOT all links of a document should be inside a <nav> element. The <nav> element is intended only for major blocks of navigation links."},

    {'li': "The <li> tag defines a list item.\nThe <li> tag is used inside ordered lists(<ol>), unordered lists (<ul>), and in menu lists (<menu>).\nIn <ul> and <menu>, the list items will usually be displayed with bullet points.\nIn <ol>, the list items will usually be displayed with numbers or letters."},

    {'a': "The <a> tag defines a hyperlink, which is used to link from one page to another."},

    {'button':
        "The <button> tag defines a clickable button.\nInside a <button> element you can put text (and tags like <i>, <b>, <strong>, <br>, <img>, etc.). \nThat is not possible with a button created with the <input> element!"},

    {'iframe': "The <iframe> tag specifies an inline frame.\nAn inline frame is used to embed another document within the current HTML document."},

    {'table': "The <table> tag defines an HTML table.\nAn HTML table consists of one <table> element and one or more <tr>, <th>, and <td> elements.\nThe <tr> element defines a table row, the <th> element defines a table header, and the <td> element defines a table cell.\nAn HTML table may also include <caption>, <colgroup>, <thead>, <tfoot>, and <tbody> elements."},

    {'td': "The <td> tag defines a standard data cell in an HTML table.\nAn HTML table has two kinds of cells:\nHeader cells - contains header information (created with the <th> element)\nData cells - contains data (created with the <td> element)\nThe text in <td> elements are regular and left-aligned by default.\nThe text in <th> elements are bold and centered by default. "},

    {'tr': "The <tr> tag defines a row in an HTML table.\nA <tr> element contains one or more <th> or <td> elements."},

    {'ul': "The <ul> tag defines an unordered (bulleted) list."},

]


def search_key(tag_dict, key):
    for item in tag_dict:
        if key in item:
            return item[key]


print(f'\n{search_key(tag_dict, 'button')}\n')
