let birdForm1 = document.querySelectorAll(".bird-form1")
let container1 = document.querySelector("#form1")
let addButton1 = document.querySelector("#add-form1")
let totalForms1 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum1 = birdForm1.length-1
addButton1.addEventListener('click', addForm1)

function addForm1(e){
    e.preventDefault()

    let newForm = birdForm1[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum1++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum1}-`)
    container1.insertBefore(newForm, addButton1)
    
    totalForms1.setAttribute('value', `${formNum1+1}`)
}




let birdForm5 = document.querySelectorAll(".bird-form5")
let container5 = document.querySelector("#form5")
let addButton5 = document.querySelector("#add-form5")
let totalForms5 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum5 = birdForm5.length-1
addButton5.addEventListener('click', addForm5)

function addForm5(e){
    e.preventDefault()

    let newForm = birdForm5[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum5++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum5}-`)
    container5.insertBefore(newForm, addButton5)
    
    totalForms5.setAttribute('value', `${formNum5+1}`)
}



