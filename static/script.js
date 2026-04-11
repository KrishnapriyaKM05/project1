async function play(player) {
    const response = await fetch(`/play/${player}`);  
    const data = await response.json();               

    document.getElementById("computer-choice").textContent = "Computer chose: " + data.computer;
    document.getElementById("result").textContent = data.result;
}