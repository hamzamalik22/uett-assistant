const toggleButton = document.getElementById("toggleButton");
const contentDiv = document.getElementById("content");

toggleButton.addEventListener("change", function () {
  if (this.checked) {
    contentDiv.style.display = "block";
  } else {
    contentDiv.style.display = "none";
  }
});
