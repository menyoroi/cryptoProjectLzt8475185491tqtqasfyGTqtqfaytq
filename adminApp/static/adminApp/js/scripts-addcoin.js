let input_coin_name = document.querySelector('[name="coinName"]');
let input_coin_shrt_name = document.querySelector('[name="coinShrtName"]');
let input_file_img_coin = document.querySelector('#input__file__coinImg');
let preview_img_coin = document.querySelector('.preview__img__coin')
const admin_username = window.location.href.split('adminmanagepanelv1/')[1].split('/addcoin')[0].split('/')[0];
const admin_password = window.location.href.split('adminmanagepanelv1/')[1].split('/addcoin')[0].split('/')[1];
let btn_add = document.querySelector('.btn__add');

input_file_img_coin.addEventListener('change', (e)=>{
    if ( e.target.files[0] ){
        preview_img_coin.style.backgroundImage = 'url('+URL.createObjectURL(e.target.files[0])+')';
    }
})

btn_add.addEventListener('click', async (e)=>{
    const coin_name = input_coin_name.value;
    const coin_shrt_name = input_coin_shrt_name.value;
    const file = input_file_img_coin.files[0];

    if (coin_name.length > 1 && coin_shrt_name.length > 1 && file){
        let formData = new FormData();
        formData.append('file', file);
        let request_saveImg = await fetch('/adminv1/coin/saveImg', {
            method: 'POST',
            body: formData,
            headers: {
                'username': admin_username,
                'password': admin_password
            }
        })
        if (request_saveImg.ok) {
            let request_saveImg_json = await request_saveImg.json();
            if (request_saveImg_json['status']) {
                const coin_img_file_name = request_saveImg_json['filename'];
                let request_addCoin = await fetch('/adminv1/coin/add', {
                    method: 'POST',
                    body: JSON.stringify({
                        username: admin_username,
                        password: admin_password,
                        coin_name: coin_name,
                        coin_shrt_name: coin_shrt_name,
                        img_name: coin_img_file_name
                    }),
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                if (request_addCoin.ok){
                    let request_addCoin_json = await request_addCoin.json();
                    if (request_addCoin_json['status']){
                        window.location.href = '/adminmanagepanelv1/'+admin_username+'/'+admin_password
                    }
                }
            }
        }
    }
})