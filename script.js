const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");
const loadingDiv = document.getElementById("loading");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const audioFile = document.getElementById("audio").files[0];
    const language = document.getElementById("language").value;

    if (!audioFile) {
        alert("Please upload an audio file");
        return;
    }

    const formData = new FormData();
    formData.append("audio", audioFile);
    formData.append("language", language);

    loadingDiv.style.display = "block";
    resultDiv.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/detect", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        loadingDiv.style.display = "none";

        resultDiv.innerHTML = `
            <h3>Result</h3>
            <p><strong>Classification:</strong> ${data.classification}</p>
            <p><strong>Confidence:</strong> ${data.confidence_score}</p>
        `;

    } catch (error) {
        loadingDiv.style.display = "none";
        resultDiv.innerHTML = "<p style='color:red'>Error connecting to backend</p>";
        console.error(error);
    }
});
