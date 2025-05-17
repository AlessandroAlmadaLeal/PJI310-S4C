// Mensagens globais associadas aos valores dos botões
const mensagens = {
    m1: "Colaborador cadastrado com sucesso!",
    m2: "Acesso ao coletivo liberado!",
    m3: "Assento reservado para a data."
};

// Aguarda o carregamento do DOM
document.addEventListener('DOMContentLoaded', function () {
    const botoes = document.querySelectorAll('button');

    botoes.forEach(function (botao) {
        botao.addEventListener('click', function (event) {
            event.preventDefault(); // Evita envio automático do formulário

            const valor = botao.value;
            const mensagem = mensagens[valor] || "Ação não reconhecida.";

            const formulario = botao.closest('form');

            if (formulario) {
                const camposObrigatorios = formulario.querySelectorAll('[required]');
                
                if (camposObrigatorios.length > 0) {
                    let camposValidos = true;

                    camposObrigatorios.forEach(function (campo) {
                        if (
                            !campo.disabled &&
                            campo.offsetParent !== null &&
                            campo.value.trim() === ''
                        ) {
                            camposValidos = false;
                        }
                    });

                    if (!camposValidos) {
                        alert("Por favor, preencha todos os campos obrigatórios.");
                        return;
                    }
                }
            }

            // Tudo certo, mostra a mensagem e redireciona
            alert(mensagem);
            window.location.href = 'intro';
        });
    });
});
