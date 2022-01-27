document.addEventListener('DOMContentLoaded', function() {

    var modalButton = document.querySelector('.js-open-modal'),
       overlay      = document.querySelector('.js-overlay-modal'),
       closeButtons = document.querySelectorAll('.js-modal-close');

    modalButton.addEventListener('click', function(e) {
        e.preventDefault();

        var modalElem = document.querySelector('.modal[data-modal="1"]');

        modalElem.classList.add('active');
        overlay.classList.add('active');
    });

    closeButtons.forEach(function(item){

      item.addEventListener('click', function(e) {
         var parentModal = this.closest('.modal');

         parentModal.classList.remove('active');
         overlay.classList.remove('active');
      });

   }); // end foreach

    // скрывается по нажатию на эскейп или на свободное пространство
    document.body.addEventListener('keyup', function (e) {
        var key = e.keyCode;

        if (key === 27) {

            document.querySelector('.modal.active').classList.remove('active');
            document.querySelector('.overlay').classList.remove('active');
        };
    }, false);


    overlay.addEventListener('click', function() {
        document.querySelector('.modal.active').classList.remove('active');
        this.classList.remove('active');
    });

});


