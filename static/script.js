const createButton = document.querySelector('.btn-success');
createButton.addEventListener('click', () => {
    createButton.classList.add('animate__animated', 'animate__bounce');
});

const blogButton = document.querySelector('.nav-link.active');
blogButton.addEventListener('click', () => {
    blogButton.classList.add('animate__animated', 'animate__bounce');
});