function calculateBMI() {
    const weight = document.getElementById("weight").value;
    const height = document.getElementById("height").value;

    if (!weight || !height) {
        document.getElementById("result").textContent = "Please enter both weight and height!";
        return;
    }

    fetch("https://bmi-api-um3h.onrender.com/bmi", {  // เปลี่ยน URL เป็นของคุณ
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ weight, height })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").textContent = `Your BMI: ${data.bmi}`;
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("result").textContent = "Error calculating BMI.";
    });
}
