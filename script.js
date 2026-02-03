const form = document.getElementById("uploadForm");
const resultDiv = document.getElementById("result");
const loadingDiv = document.getElementById("loading");
const fileInput = document.getElementById("audio");
const fileLabel = document.getElementById("file-label");

// Show file name when selected
fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        fileLabel.innerText = `📄 ${fileInput.files[0].name}`;
        fileLabel.style.color = "#00f2ff";
    }
});

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const audioFile = fileInput.files[0];
    const language = document.getElementById("language").value;

    if (!audioFile) {
        alert("Integrity Error: No audio file detected.");
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

        // Epic Result Display
        resultDiv.innerHTML = `
            <div class="result-card">
                <h3 style="color: #7000ff">ANALYSIS COMPLETE</h3>
                <p><strong>Identity:</strong> <span style="color: #00f2ff">${data.classification}</span></p>
                <p><strong>Confidence:</strong> ${Math.round(data.confidence_score * 100)}%</p>
            </div>
        `;

    } catch (error) {
        loadingDiv.style.display = "none";
        resultDiv.innerHTML = "<p style='color:#ff4444'>CRITICAL ERROR: Connection Terminated</p>";
        console.error(error);
    }
});