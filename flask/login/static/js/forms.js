const formImageElement = document.querySelectorAll('.form-image')
const allPasswordIcons = document.querySelectorAll(".fa-regular");

allPasswordIcons.forEach((icon) => {
    icon.addEventListener('click', () => {
        const input = icon.parentElement.querySelector("input")
        if (input.getAttribute("type") === 'password'){
            input.setAttribute('type', 'text')
            icon.classList.remove('fa-eye-slash')
            icon.classList.add('fa-eye')

        } else {
            input.setAttribute('type', 'password')
            icon.classList.add('fa-eye-slash')
            icon.classList.remove('fa-eye')
        }
    })
})

const images = [ 
    "https://images.pexels.com/photos/7552741/pexels-photo-7552741.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/3762940/pexels-photo-3762940.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/7552326/pexels-photo-7552326.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
    "https://images.pexels.com/photos/7552724/pexels-photo-7552724.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
]

const htmlCreatedImage = images.map((ImageLink) => {
    return `
    <img src=${ImageLink} alt='login images' />
    `
})

formImageElement.forEach((formGroupImage) => {
    formGroupImage.innerHTML = htmlCreatedImage.join("")
})



