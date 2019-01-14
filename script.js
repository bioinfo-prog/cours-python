$("pre > code").each(function(index, codeElement) {
  var formattedCode = $(codeElement).html().replace("\r\n", "\n").split("\n");

  var codeLength = formattedCode.length;
  $(codeElement).text("");
  $.each(formattedCode, function(index, line) {
    $(codeElement).append("<span>" + line + "</span>\n");
    if (codeLength - 1 == index) return;
  });
});
