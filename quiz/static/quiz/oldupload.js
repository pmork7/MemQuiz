let fileUpload = document.getElementById("id_file");
console.log(fileUpload);

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
    let i = 0;
    for (i = 0; i < items.length; i++) {
      let p = document.createElement("p");
      p.textContent = items[i];
      document.body.appendChild(p);
    }


  })();
});
