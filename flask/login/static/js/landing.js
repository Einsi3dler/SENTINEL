const menuIcon = document.getElementById('menu-icon');
const menuItems = document.getElementById('menu-items');
const overLay = document.getElementById('overlay');
const faqBoxIcons = document.querySelectorAll('.faq-box .icon')
const faqBox = document.querySelectorAll('.faq-box')



const close = '<svg xmlns="http://www.w3.org/2000/svg" height="40px" viewBox="0 -960 960 960" width="35px" fill="#5f6368"><path d="m251.33-204.67-46.66-46.66L433.33-480 204.67-708.67l46.66-46.66L480-526.67l228.67-228.66 46.66 46.66L526.67-480l228.66 228.67-46.66 46.66L480-433.33 251.33-204.67Z"/></svg>'
const open = '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="35px" fill="#5f6368"><path d="M120-240v-80h720v80H120Zm0-200v-80h720v80H120Zm0-200v-80h720v80H120Z"/></svg>'

const toggleMenu = () => {
    if (menuItems.classList.contains('show-menu-small-screen')) {
        menuItems.classList.toggle('show-menu-small-screen')
        overLay.classList.toggle('overlay')
        menuIcon.innerHTML = open;
    } else {
        menuItems.classList.toggle('show-menu-small-screen')
        overLay.classList.toggle('overlay')
        menuIcon.innerHTML = close
    }
}

const removeShowFaqs = () => {
    faqBox.forEach((box) => {
        box.classList.remove('show-faqs')
    })
}

faqBox.forEach((box) => {    
    box.addEventListener('click', () => {
        if (box.classList.contains('show-faqs')) {
            box.classList.remove('show-faqs')
        } else {
            removeShowFaqs()
            box.classList.add('show-faqs')
        }
    })
})


menuIcon.onclick = toggleMenu
overLay.onclick = toggleMenu