const url = 'http://127.0.0.1:8000/api/mobile/';
const url_post = 'http://127.0.0.1:8000/api/mobile/add/';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

async function loadMobile() {
    console.log("mobiles loading......");
    const response = await fetch(url);
    const mobiles = await response.json();
    console.log("mobiles fetched", mobiles);

    const mobileList = document.getElementById('mobile-list');
    mobileList.innerHTML = '';

    mobiles.forEach(mobile => {
        const mobileDiv = document.createElement('div');
        mobileDiv.innerHTML = `
            <h3>${mobile.brand_name}</h3>
            <p>Price: ${mobile.price}</p>
            <button onclick="deleteMobile(${mobile.id})">Delete</button>
        `;
        mobileList.appendChild(mobileDiv);
    });
}

document.getElementById('add-new-mobiles').addEventListener('submit', async function (e) {
    e.preventDefault();
    const brand_name = document.getElementById('brand-name').value;
    const price = document.getElementById('mobile-price').value;

    const response = await fetch(url_post, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            brand_name: brand_name,
            price: price
        })
    });

    if (response.ok) {
        console.log("Mobile added successfully");
        loadMobile(); // refresh list after adding
        document.getElementById('add-new-mobiles').reset(); // reset form
    } else {
        console.error("Failed to add mobile");
    }
});

// delete mobile function
async function deleteMobile(id) {
    const confirmDelete = confirm("Are you sure you want to delete?");
    if (!confirmDelete) return;

    const response = await fetch(`http://127.0.0.1:8000/api/mobile/${id}/delete/`, {
        method: 'DELETE',
        headers: {
            'X-CSRFToken': csrftoken,
        }
    });

    if (response.ok) {
        console.log("Mobile deleted successfully");
        loadMobile(); // refresh list after deleting
    } else {
        console.error("Failed to delete mobile");
    }
}

// Load mobiles when page loads
loadMobile();
