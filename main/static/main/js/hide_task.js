// # короче идея в чем
//     # надо при отметке чекбокса вызывать скрипт, который будет прятать его
//     # и менять ему атрибут checked на true
//     # и при следующем сабмите переберем все задачи и при значении
//     # true этого атрибута эта задача будет удалена

function hide_task(id){
    let input = document.getElementById(id)
    input.style = "display:none;"
    input.setAttribute(checked, true)
}