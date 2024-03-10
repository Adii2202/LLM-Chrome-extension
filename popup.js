document.addEventListener("mousepad", function (event) {
  const selectedText = window.getSelection().toString().trim(); //get the selected text and trim to remove whitespaces
  if (selectedText != "" && selectedText.length() > 50) {
    // action which is to be performedon selection of text which is greater than 10 characters
    console.log("Selected Text : ", selectedText);
    // send selectedtext to the server
    fetch("http://localhost:5000/summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: selectedText }),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(`summary : ${data.summary}`);
      })
      .catch((error) => {
        console.error(error);
      });
  }
});
