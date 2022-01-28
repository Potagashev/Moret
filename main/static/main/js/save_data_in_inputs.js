document.addEventListener("DOMContentLoaded", function() { // событие загрузки страницы

    // выбираем на странице все элементы типа textarea и input
    let inputs = document.querySelectorAll('textarea, input');

    for (let i=0; i < inputs.length; i++){
        if(inputs[i].id === 'add_task_input') {continue;} // если это инпут с добавлением задач, скипаем
        // если данные значения уже записаны в sessionStorage, то вставляем их в поля формы
        // путём этого мы как раз берём данные из памяти браузера, если страница была случайно перезагружена
        if(inputs[i].value === '') inputs[i].value = window.sessionStorage.getItem(inputs[i].name, inputs[i].value);
        // на событие ввода данных (включая вставку с помощью мыши) вешаем обработчик
        inputs[i].addEventListener('input', function() {
            // и записываем в sessionStorage данные, в качестве имени используя атрибут name поля элемента ввода
            window.sessionStorage.setItem(inputs[i].name, inputs[i].value);
        })
    }
});