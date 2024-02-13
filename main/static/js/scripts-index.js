let login_btns = document.querySelectorAll('.btn.login');
let reg_btns = document.querySelectorAll('.btn.register');
let list_reg_login_btns = [reg_btns, login_btns];
let window_auth = document.querySelector('.window__auth');
let close = window_auth.querySelector('.window__auth__ico__close');
let link_reg = window_auth.querySelector('.window__auth__link')
let body = document.body;

const request_auth = async (type='login')=>{
    const input_email = window_auth.querySelector('[name="email"]');
    const input_password = window_auth.querySelector('[name="password"]');
    const securityKey = document.querySelector('securitykey');
    let request =  fetch('/auth/'+type,{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            email: input_email.value,
            password: input_password.value,
            securityKey: securityKey.getAttribute('key')
        })
    });
    return request;
}

close.addEventListener('click', (e)=>{
    window_auth.style.display = 'none';
    body.style.overflowY = 'scroll';
})

if ( document.querySelector('.header .auth__btns')){
    list_reg_login_btns.map((elements)=>{
        elements.forEach((element)=>{
            if( !element.className.includes('form') ) {
                element.addEventListener('click', (e) => {
                    window_auth.style.display = 'flex';
                    body.style.overflowY = 'hidden';
                    let input_mail_auth_form = window_auth.querySelector('[name="email"]');
                    input_mail_auth_form.value = '';
                    let reg_form_input_email_on_page = e.target.parentNode.querySelector('.reg__form input[name="email"]');
                    if (reg_form_input_email_on_page) {
                        input_mail_auth_form.value = reg_form_input_email_on_page.value;
                    }
                });
            }
        });
    })
}

link_reg.addEventListener('click', (e)=>{
    let window_auth_btn = window_auth.querySelector('.btn');
    let window_auth_header = window_auth.querySelectorAll('.form__auth__inner label')[0];
    if (window_auth_btn.className.includes('login')){
        window_auth_btn.classList.remove('login');
        window_auth_btn.classList.add('register');
        window_auth_btn.innerText = 'Register';
        window_auth_header.innerText = 'Registration';
        e.target.innerText = 'Login';
    }
    else {
        window_auth_btn.classList.remove('register');
        window_auth_btn.classList.add('login');
        window_auth_btn.innerText = 'Login';
        window_auth_header.innerText = 'Authorization';
        e.target.innerText = 'Registration';
    }
})

window_auth.querySelector('.btn.form').addEventListener('click',async (e)=>{
    let type = 'reg';
    if (e.target.className.includes('login')){
        type = 'login';
    }
    request_auth(type).then((response)=>{
        if (response.ok){
            return response.json();
        }
    }).then((data)=>{
        if (data['auth']){
            window.location.href = '/';
        }
        else {
            window.alert(data['error']);
        }
    });
})