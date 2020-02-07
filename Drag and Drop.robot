https://stackoverflow.com/questions/49571152/robotframework-drag-and-drop-selenium2-keyword-seems-not-to-work

Drag and Drop

https://stackoverflow.com/questions/49864965/org-openqa-selenium-elementnotinteractableexception-element-is-not-reachable-by

https://stackoverflow.com/questions/41978952/how-to-use-fully-functional-jsonpath-in-robotframework
=======================Java Script=========================================
https://stackoverflow.com/questions/3813294/how-to-get-element-by-innertext
Execute Javascript	  *code
Executes the given JavaScript code.
document.getElementById('foo')


=============
Examples:

Execute JavaScript	 window.my_js_function('arg1', 'arg2')
Execute JavaScript	 ${CURDIR}/js_to_execute.js
${sum}=	Execute JavaScript	 return 1 + 1;
Should Be Equal	  ${sum}	 ${2}

=============
Example2:

JS Click Element
[Arguments]     ${element_xpath}
${element_xpath}=       //*[text()='A3']
Execute JavaScript  document.evaluate("${element_xpath}", document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null).snapshotItem(0).click();

=============
document.evaluate("//*[text()='A3']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue

You could save a lot of space by using 9 instead of XPathResult.FIRST_ORDERED_NODE_TYPE.
document.evaluate("//*[text()='A3']", document, null, 9, null).singleNodeValue

=============
Instead of finding element and then passing to JS, you can directly find element by ID and click it using JS.
Execute JavaScript    document.getElementById("element-id").onclick()

=============
var headings = document.evaluate("/html/body//h2", document, null, XPathResult.ANY_TYPE, null);
/* Search the document for all h2 elements.
 * The result will likely be an unordered node iterator. */
var thisHeading = headings.iterateNext();
=============
