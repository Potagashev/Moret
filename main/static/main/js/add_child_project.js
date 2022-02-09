let isEmpty = true
function child_project_form(btn_id, p_id){
  if(isEmpty) {
    let add_child_project = document.getElementById(btn_id)
    add_child_project.parentNode.removeChild(add_child_project)

    let div = document.createElement('div');

    let title = document.createElement('h3');
    title.innerText = 'Подзадачи'

    let p1 = document.createElement('p');
    p1.innerHTML = `Название<br>`
    let name = document.createElement("input");
    name.name = 'subproject_name'
    p1.appendChild(name)

    let p2 = document.createElement("p");
    p2.innerHTML = 'Описание<br>'
    let description = document.createElement("textarea");
    description.name = 'subproject_description'
    p2.appendChild(description)

    let p3 = document.createElement("p");
    p3.innerHTML = 'Дедлайн<br>'
    let deadline = document.createElement("input");
    deadline.name = 'subproject_deadline'
    deadline.type = "datetime-local"
    p3.appendChild(deadline)

    let button = document.createElement('button');
    button.innerText = 'Готово'
    button.type = 'commit'
    button.class = 'del-edit';

    div.appendChild(title)
    div.appendChild(p1);
    div.appendChild(p2);
    div.appendChild(p3);
    div.appendChild(button);

    let before_btn = document.getElementById(p_id)
    before_btn.appendChild(div)
    isEmpty = false
  }
}

function show_details(pr_name, pr_description, pr_deadline){
  let btn = document.getElementById(`button_${pr_name}`)
  btn.innerHTML = '<svg style="width: 14px; height: 14px;" class="arrow-bottom-2" viewBox="0 0 9 14">\n' +
      '    <path class="svg-arrow" d="M6.660,8.922 L6.660,8.922 L2.350,13.408 L0.503,11.486 L4.813,7.000 L0.503,2.515 L2.350,0.592 L8.507,7.000 L6.660,8.922 Z" />\n' +
      '</svg>'
  btn.onclick = function(){hide_details(pr_name, pr_description, pr_deadline)}

  let p = document.getElementById(pr_name)
  let div = document.createElement('div')
  div.id = `div_${pr_name}`
  div.style = 'margin-left: 27.5px;'
  div.innerHTML = `<p>${pr_description}</p>Срок выполнения: ${pr_deadline}`
  p.appendChild(div)
}

function hide_details(pr_name, pr_description, pr_deadline){
  let btn = document.getElementById(`button_${pr_name}`)
  btn.innerHTML = '<svg style="width: 14px; height: 14px;" class="arrow-right-2" viewBox="0 0 9 14">\n' +
      '    <path class="svg-arrow" d="M6.660,8.922 L6.660,8.922 L2.350,13.408 L0.503,11.486 L4.813,7.000 L0.503,2.515 L2.350,0.592 L8.507,7.000 L6.660,8.922 Z" />\n' +
      '</svg>'
  btn.onclick = function(){show_details(pr_name, pr_description, pr_deadline)}

  let p = document.getElementById(pr_name)
  let div = document.getElementById(`div_${pr_name}`)
  p.removeChild(div)
}