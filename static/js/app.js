Page = {
    init: function () {
        Telegram.WebApp.ready();

        let initData = Telegram.WebApp.initData || '';
        if (initData === '') {
            return document.getElementsByTagName('body').innerHTML = 'Iltimos bot orqali ro\'yxatdan o\'ting!'
        }
        Telegram.WebApp.enableClosingConfirmation()
        Telegram.WebApp.expand()
        document.getElementById('auth').value = initData
        let main_button = Telegram.WebApp.MainButton;
        main_button.setText("Ro'yxatdan o'tish")
        main_button.show()
        main_button.onClick(function () {
            main_button.showProgress()
            document.getElementById('signup-button').click()
            main_button.hideProgress()
        })
    },

    success_page: function () {
        Telegram.WebApp.ready();
        Telegram.WebApp.disableClosingConfirmation()
        let main_button = Telegram.WebApp.MainButton;
        main_button.show()
        main_button.setText("Yopish")
        main_button.onClick(function () {
            Telegram.WebApp.close()
        })
    },
}

function check_form () {
    let form = document.getElementById('signup-form');
    let fields = form.querySelectorAll('input, select, textarea');
    for (let field of fields) {
        if (field.required && !field.value.trim()) {
            return false;
        }
    }
    return true;
}