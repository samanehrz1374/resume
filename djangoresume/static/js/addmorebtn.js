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


let birdForm2 = document.querySelectorAll(".bird-form2")
let container2 = document.querySelector("#form3")
let addButton2 = document.querySelector("#add-form2")
let totalForms2 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum2 = birdForm2.length-1
addButton2.addEventListener('click', addForm2)

function addForm2(e){
    e.preventDefault()

    let newForm = birdForm2[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum2++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum2}-`)
    container2.insertBefore(newForm, addButton2)
    
    totalForms2.setAttribute('value', `${formNum2+1}`)
}



let birdForm3 = document.querySelectorAll(".bird-form3")
let container3 = document.querySelector("#form5")
let addButton3 = document.querySelector("#add-form3")
let totalForms3 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum3 = birdForm3.length-1
addButton3.addEventListener('click', addForm3)

function addForm3(e){
    e.preventDefault()

    let newForm = birdForm3[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum3++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum3}-`)
    container3.insertBefore(newForm, addButton3)
    
    totalForms3.setAttribute('value', `${formNum3+1}`)
}



let birdForm4 = document.querySelectorAll(".bird-form4")
let container4 = document.querySelector("#form7")
let addButton4 = document.querySelector("#add-form4")
let totalForms4 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum4 = birdForm4.length-1
addButton4.addEventListener('click', addForm4)

function addForm4(e){
    e.preventDefault()

    let newForm = birdForm4[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum4++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum4}-`)
    container4.insertBefore(newForm, addButton4)
    
    totalForms4.setAttribute('value', `${formNum4+1}`)
}


let birdForm5 = document.querySelectorAll(".bird-form5")
let container5 = document.querySelector("#form9")
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


let birdForm6 = document.querySelectorAll(".bird-form6")
let container6 = document.querySelector("#form11")
let addButton6 = document.querySelector("#add-form6")
let totalForms6 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum6 = birdForm6.length-1
addButton6.addEventListener('click', addForm6)

function addForm6(e){
    e.preventDefault()

    let newForm = birdForm6[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum6++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum6}-`)
    container6.insertBefore(newForm, addButton6)
    
    totalForms6.setAttribute('value', `${formNum6+1}`)
}



let birdForm7 = document.querySelectorAll(".bird-form7")
let container7 = document.querySelector("#form13")
let addButton7 = document.querySelector("#add-form7")
let totalForms7 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum7 = birdForm7.length-1
addButton7.addEventListener('click', addForm7)

function addForm7(e){
    e.preventDefault()

    let newForm = birdForm7[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum7++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum7}-`)
    container7.insertBefore(newForm, addButton7)
    
    totalForms7.setAttribute('value', `${formNum7+1}`)
}




let birdForm8 = document.querySelectorAll(".bird-form8")
let container8 = document.querySelector("#form15")
let addButton8 = document.querySelector("#add-form8")
let totalForms8 = document.querySelector("#id_form-TOTAL_FORMS")

let formNum8 = birdForm8.length-1
addButton8.addEventListener('click', addForm8)

function addForm8(e){
    e.preventDefault()

    let newForm = birdForm8[0].cloneNode(true)
    let formRegex = RegExp(`form-(\\d){1}-`,'g')

    formNum8++
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum8}-`)
    container8.insertBefore(newForm, addButton8)
    
    totalForms8.setAttribute('value', `${formNum8+1}`)
}


