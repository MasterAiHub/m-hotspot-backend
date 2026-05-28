const API_BASE = '/api/v1';

async def redeemVoucher() {
    const code = document.getElementById('voucher-code').value;
    const statusMsg = document.getElementById('status-msg');
    
    if (!code) {
        statusMsg.innerText = "Please enter a code";
        statusMsg.style.color = "red";
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/vouchers/redeem`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                code: code,
                mac_address: '00:00:00:00:00:00' // Placeholder for actual MAC
            })
        });

        const data = await response.json();

        if (response.ok) {
            statusMsg.innerText = "Success! Connecting...";
            statusMsg.style.color = "#00ff00";
            setTimeout(() => {
                window.location.href = 'dashboard.html';
            }, 2000);
        } else {
            statusMsg.innerText = data.detail || "Invalid Voucher";
            statusMsg.style.color = "red";
        }
    } catch (error) {
        statusMsg.innerText = "Connection error";
        statusMsg.style.color = "red";
    }
}

// Simulated active users counter
setInterval(() => {
    const el = document.getElementById('active-users');
    if (el) {
        const current = parseInt(el.innerText);
        const change = Math.floor(Math.random() * 5) - 2;
        el.innerText = Math.max(100, current + change);
    }
}, 3000);
