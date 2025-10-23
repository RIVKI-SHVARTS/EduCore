
function showAlert(msg, type = "info", duration = 2000, onConfirm, onCancel) {
    const alertDiv = document.createElement("div");
    if (type === "confirm") {
        alertDiv.className = `alert-container alert-confirm`;
    } else {
        alertDiv.className = `alert-container alert-${type}`;
    }
    
    const message = document.createElement("div");
    message.textContent = msg;
    alertDiv.appendChild(message);

  
    if (type === "confirm") {
        const btnContainer = document.createElement("div");
        btnContainer.className = "alert-buttons";

        const btnConfirm = document.createElement("button");
        btnConfirm.textContent = "delete";
        btnConfirm.className = "btn-confirm";

        const btnCancel = document.createElement("button");
        btnCancel.textContent = "cancele";
        btnCancel.className = "btn-cancel";

        btnConfirm.addEventListener("click", () => {
            alertDiv.remove();
            if (onConfirm) onConfirm();
        });

        btnCancel.addEventListener("click", () => {
            alertDiv.remove();
            if (onCancel) onCancel();
        });

        btnContainer.appendChild(btnConfirm);
        btnContainer.appendChild(btnCancel);
        alertDiv.appendChild(btnContainer);
    }

    document.body.appendChild(alertDiv);

   
    requestAnimationFrame(() => {
        alertDiv.style.opacity = "1";
        alertDiv.style.transform = "translateX(-50%) translateY(0)";
    });

    
    if (type !== "confirm") {
        setTimeout(() => {
            alertDiv.style.opacity = "0";
            alertDiv.style.transform = "translateX(-50%) translateY(-20px)";
            setTimeout(() => alertDiv.remove(), 400);
        }, duration);
    }
}
