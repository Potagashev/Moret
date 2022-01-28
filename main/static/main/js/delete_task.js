function delete_task(task_id){
    let btn = document.getElementById(task_id)

    btn.addEventListener('click', function (event) {
        event.preventDefault();

        let form = document.createElement('form');
        form.method = 'GET';

        let input = document.createElement('input')
        input.name = task_id
        input.hidden

        form.append(input)

        document.body.append(form);

        form.submit();
    })
}