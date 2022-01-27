function delete_project(project_id){
    let form = document.createElement('form');
    form.method = 'GET';

    input = document.createElement('input')
    input.name = project_id
    input.hidden

    form.append(input)

    // перед отправкой формы, её нужно вставить в документ
    document.body.append(form);

    form.submit();
}
