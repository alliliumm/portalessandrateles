/* Abre e fecha menu lateral em modo mobile */
const menuMobile = document.querySelector('.menu-mobile')
const body =  document.querySelector('body')
const menuClick = document.querySelectorAll('.nav-item')

function abrirFecharMenu(){
    menuMobile.classList.contains("bi-list") // classList: Minha lista de classes que contém esta classe no HTML
    ? menuMobile.classList.replace("bi-list", "bi-x")
    : menuMobile.classList.replace("bi-x","bi-list");

    body.classList.toggle("menu-nav-active") 
    // Verifica se a classe "menu-nav-active" está presente no elemento e ativa ou desativa o menu lateral
}

menuMobile.addEventListener('click',abrirFecharMenu)// Adiconando evento ao clicar
menuClick.forEach(item => {
    item.addEventListener('click',abrirFecharMenu) // Adiconando evento ao clicar
})

/* Animação com atributo data-anime */
const item = document.querySelectorAll("[data-anime]");

const animeScroll = () => {
    const windowTop  = window.scrollY + window.innerHeight * 0.85 // Pegar o eixo y atual topo, um pouco antes de chegar o topo

    item.forEach(element => { // Cada data-anime
        if(windowTop > element.offsetTop){ // For maior que a altura deste data-anime no topo
            element.classList.add("animate"); // Adiciona classe estilizada
        }else{
            element.classList.remove("animate"); // Remove classe estilizada
        }
    })
}
animeScroll()
window.addEventListener("scroll", animeScroll)

// ACTIONS -> ENVIO DE E-MAIL
const btnEnviar =  document.querySelector('#btn-enviar')
const form = document.getElementById('form');
const alerta  = document.getElementById('alerta');
const iconAlerta = document.getElementById('iconAlerta')
const message  = document.getElementById('message');
const closeButton = document.getElementById('closeButton');

// Funções de Mudanças Dinâmicas

function iniciarLoading(){
    btnEnviar.disabled = true;
    spanLoading = 
        '<span class="spinner-border spinner-border-sm" aria-hidden="true"></span>'+
        '<span role="status"> Enviando...</span>';
    btnEnviar.innerHTML = spanLoading;
}
function terminarLoading(){
    spanText = '<span role="status">Enviar mensagem</span>';
    btnEnviar.disabled = false;
    btnEnviar.innerHTML = spanText;
}
function alertModal(response){
    if(response){
        alerta.className = alerta.className.replace(/\b(alert-warning|alert-danger)\b/g, 'alert-success');
        iconAlerta.className = iconAlerta.className.replace('bi-exclamation-circle-fill', 'bi-check-circle-fill');
    }else{
        alerta.className = alerta.className.replace(/\b(alert-success|alert-warning)\b/g, 'alert-danger');
        iconAlerta.className = iconAlerta.className.replace('bi-check-circle-fill', 'bi-exclamation-circle-fill');
    }
}
function limpezaCampos(){
    document.querySelector('#nome').value = '';
    document.querySelector('#assunto').value = '';
    document.querySelector('#email').value = '';
    document.querySelector('#mensagem').value = '';
}
function alertTemporizado(){
    // Sumir o alerta depois de 5seg
    setTimeout(() => {
        alerta.style.display = 'none'
    }, 5000)
}

form.addEventListener('submit', async (event) => {
    event.preventDefault();

    // Validação de campos
    const formData = new FormData(form);
    valuesFormData = [];
    count = 0;
    for (let pair of formData.entries()) {
        count += 1;
        if(pair[1]){
            valuesFormData.push(pair[1])
        }
    }

    if(count == valuesFormData.length){
        iniciarLoading();

        // POST 
        const response = await fetch('/send',{
            method: 'POST',
            body: formData
        });

        if(response.ok){ //200 OK
            const data = await response.json();
            alertModal(data.success);
            resultadoEnvio = data.success;
            message.textContent = data.message;
        }else{
            alertModal(response.ok)
            message.textContent = 'Erro ao enviar o formulário. Por favor, tente novamente mais tarde.';
        }

        alerta.style.display = 'block';

        terminarLoading();
        limpezaCampos();
        alertTemporizado();
        setTimeout(() => {
            if(resultadoEnvio){
                alertModal(resultadoEnvio);
                message.textContent = 'Verifique sua caixa de entrada para mais detalhes.';
                alerta.style.display = 'block'
                alertTemporizado();
            }
        }, 6000)
    }
});

// Fechar o alerta 
closeButton.addEventListener('click', () => {
    alerta.style.display = 'none'; 
});