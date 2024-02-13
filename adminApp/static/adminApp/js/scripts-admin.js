let btns_delete = document.querySelectorAll('.delete');
let coin__visibles = document.querySelectorAll('[name="coin__visible"]');
const admin_username = window.location.href.split('adminmanagepanelv1/')[1].split('/')[0];
const admin_password = window.location.href.split('adminmanagepanelv1/')[1].split('/')[1];
console.log(admin_username, admin_password)

coin__visibles.forEach((element)=>{
    element.addEventListener('change', async (e)=>{
        let coin = e.target.parentNode;
        let status_visible = e.target.checked;
        let request = await fetch('/adminv1/coin/visible', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                asset_id: coin.id,
                username: admin_username,
                password: admin_password,
                asset_status: status_visible
            })
        });
        if (request.ok){
            let request_json = await request.json();
            window.alert(request_json['status']);
        }
    })
})


btns_delete.forEach((element)=>{
    element.addEventListener('click', async (e)=>{
        let user = e.target.parentNode;
        let request = await fetch('/adminv1/user/delete', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                user_id: user.id,
                username: admin_username,
                password: admin_password
            })
        });
        if (request.ok){
            let request_json = await request.json();
            if (request_json['status'] !== 'Error'){
                user.remove();
            }
            else {
                window.alert(request_json['status']);
            }
        }
    })
})

