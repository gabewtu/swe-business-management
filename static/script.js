function login() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    fetch('/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            data.success ? "Login successful!" : "Login failed.";
    });
}

function employeeLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    fetch('/employee-login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText =
            data.success ? "Employee login successful!" : "Employee login failed.";
    });
}

function goToEmployeeLogin() {
    window.location.href = "/employee";
}