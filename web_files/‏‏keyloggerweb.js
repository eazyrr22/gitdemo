function login() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var errorMessage = document.getElementById("error-message");

    fetch("/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert("ברוך הבא, " + username + " מתחבר!");
            window.location.href = "select_computer.html"; // מעבר לדף הבא
        } else {
            errorMessage.innerText = "שם משתמש או סיסמה שגויים!";
        }
    })
    .catch(error => console.error("Error:", error));
}



document.addEventListener("DOMContentLoaded", function () {
    const select = document.getElementById("computerList");

    // ---- טעינת מחשבים מהשרת ----
    function loadComputers() {
        fetch("/get_computers")
            .then(response => response.json())
            .then(data => {
                select.innerHTML = "";
                data.computers.forEach(computer => {
                    let option = document.createElement("option");
                    option.text = computer;
                    select.add(option);
                });
            })
            .catch(error => console.error("Error fetching computers:", error));
    }

    // ---- הוספת מחשב ----
    document.getElementById("addComputer").addEventListener("click", function () {
        let computerName = prompt("Enter the new computer name:");
        if (computerName) {
            fetch("/add_computer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: computerName })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    let option = document.createElement("option");
                    option.text = computerName;
                    select.add(option);
                } else {
                    alert("Error adding computer.");
                }
            })
            .catch(error => console.error("Error adding computer:", error));
        }
    });

    // ---- הסרת מחשב ----
    document.getElementById("removeComputer").addEventListener("click", function () {
        if (select.selectedIndex !== -1) {
            let computerName = select.options[select.selectedIndex].text;

            fetch("/remove_computer", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name: computerName })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    select.remove(select.selectedIndex);
                } else {
                    alert("Error removing computer.");
                }
            })
            .catch(error => console.error("Error removing computer:", error));
        } else {
            alert("No computer selected for removal!");
        }
    });

    // ---- שליחת נתונים מוצפנים לשרת ----
    document.getElementById("sendData").addEventListener("click", function () {
        let selectedComputer = select.value;
        if (!selectedComputer) {
            alert("Please select a computer first!");
            return;
        }

        let encryptedText = prompt("Enter the encrypted text:");
        if (!encryptedText) return;

        fetch("/upload", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                computer_name: selectedComputer,
                file_name: `${selectedComputer}.txt`,
                encrypted_text: encryptedText
            })
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error("Error uploading data:", error));
    });

    // ---- קבלת נתונים מפוענחים משרת Flask ----
    document.getElementById("getData").addEventListener("click", function () {
        let selectedComputer = select.value;
        if (!selectedComputer) {
            alert("Please select a computer first!");
            return;
        }

        fetch(`/get_data/${selectedComputer}`)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert("No data found for this computer.");
                } else {
                    alert(`Decrypted Data: \n${data.data}`);
                }
            })
            .catch(error => console.error("Error fetching data:", error));
    });

    // ---- טעינת רשימת מחשבים עם פתיחת הדף ----
    loadComputers();
});
