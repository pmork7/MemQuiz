let fileUpload = document.getElementById("id_file");
let selector = document.getElementById("id_selector");
let d = document.getElementById("preview-content");


fileUpload.addEventListener("change", function() {
  let file = this.files[0];

  const streamToText = async (blob) => {
    const readableStream = await blob.getReader();
    const chunk = await readableStream.read();

    return new TextDecoder("utf-8").decode(chunk.value);
  }

  (async () => {
    const fileContentStream = await file.stream();
    const fileText = await file.text();
    let items = fileText.split("\n");
    console.log(items);
    //console.log(await streamToText(fileContentStream));
    if (d.children.length > 0) {
      while (d.children.length > 0) {
        d.removeChild(d.firstChild);
      }
    }
    let i = 0;
    for (i = 0; i < items.length; i++) {
      let p = document.createElement("p");
      p.textContent = items[i];
      d.appendChild(p);
    }
  })();
});

selector.addEventListener("click", function() {
  let delimiter = selector.value;
  let pElements = document.getElementsByTagName("p");

  function clearHighlighting() {
    let i = 0;
    for (i = 0; i < pElements.length; i++) {
      let targetIndex = pElements[i].innerHTML.indexOf('<mark>');
      if (targetIndex != -1) {
        pElements[i].innerHTML = pElements[i].innerHTML.slice(0, targetIndex) + pElements[i].innerHTML.slice(targetIndex + 6, pElements[i].innerHTML.length);
      }
      targetIndex = pElements[i].innerHTML.indexOf('</mark>');
      if (targetIndex != -1) {
        pElements[i].innerHTML = pElements[i].innerHTML.slice(0, targetIndex) + pElements[i].innerHTML.slice(targetIndex + 6, pElements[i].innerHTML.length);
      }
    }
  }

  clearHighlighting();
  let i = 0;
  for (i = 0; i < pElements.length; i++) {
    let targetIndex = pElements[i].textContent.indexOf(delimiter);
    if (targetIndex != -1) {
      pElements[i].innerHTML = pElements[i].innerHTML.slice(0, targetIndex) + "<mark>" + pElements[i].innerHTML.slice(targetIndex, targetIndex + 1) +
                                "</mark>" + pElements[i].innerHTML.slice(targetIndex + 1, pElements[i].length);
    }
    console.log(targetIndex);
  }
})
