document.addEventListener('DOMContentLoaded', function(e){
    var modals = document.querySelectorAll('.modal')
    var modalOpeners = document.querySelectorAll('.modal-opener')
    var messages = document.querySelectorAll('.messages')

    if (messages.length > 0) {
        setTimeout(() => {
            messages[0].style.display = 'none'
        }, 5000);
    }

    for (const modalOpener of modalOpeners) {
        if (modalOpener.dataset.modalId) {
            modalOpener.addEventListener('click', () => {
                var modal = document.getElementById(modalOpener.dataset.modalId)

                modal.classList.remove('modal-hide')
            })
        }
    }

    for (const modal of modals) {
        modal.addEventListener('click', function(e) {
            const target = e.target

            if (target.parentNode.classList.length == 0) {
                target.classList.add('modal-hide')
            }
        });
    }
});