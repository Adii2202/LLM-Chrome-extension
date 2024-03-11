document.getElementById("submitButton").addEventListener("click", function () {
  const prompt = document.getElementById("promptInput").value.trim();
  const selectedText = window.getSelection().toString().trim();
  if (prompt !== "" && selectedText !== "") {
    fetch("http://localhost:5000/summary", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ prompt: prompt, text: selectedText }),
    })
      .then((response) => response.json())
      .then((data) => {
        alert(`Summary: ${data.summary}`);
      })
      .catch((error) => {
        console.error(error);
      });
  } else {
    alert("Please enter a prompt and select text.");
  }
});
