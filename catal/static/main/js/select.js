// --------------------- Created By InCoder ---------------------
let customInput1 = document.querySelector('.customInput1')
selectedData1 = document.querySelector('.selectedData1')
searchInput1 = document.querySelector('.searchInput1 input')
ul1 = document.querySelector('.options1 .ul1')
customInputContainer1 = document.querySelector('.customInputContainer1')

window.addEventListener('click', (e) => {
    if (document.querySelector('.searchInput1').contains(e.target)) {
        document.querySelector('.searchInput1').classList.add('focus')
    } else {
        document.querySelector('.searchInput1').classList.remove('focus')
    }
})
$.ajax('brands', {
    dataType: 'json',
    type: 'GET',
    success: (res) => {
        // console.log(res['list']);
        // console.log(array1)
        let array1 = res['list']
        get_list(array1)
    }
})
// var array1 = [
//     "Custom Input",
//     "Mali",
//     "Vanuatu",
//     "Venezuela",
//     "Viet Nam",
//     "Virgin Islands, British",
//     "Virgin Islands, U.s.",
//     "Wallis and Futuna",
//     "Western Sahara",
//     "Yemen",
//     "Zambia",
//     "Zimbabwe"
// ];

customInput1.addEventListener('click', () => {
    console.log('hello');
    customInputContainer1.classList.toggle('show')
})

// let array1Length = array1.length

// for (let i = 0; i < array1Length; i++) {
//     let country = array1[i]
//     const li = document.createElement("li");
//     const countryName = document.createTextNode(country);
//     li.appendChild(countryName);
//     ul1.appendChild(li);
// }
function get_list(array) {
    arrayLength = array.length
for (let i = 0; i < arrayLength; i++) {
    let country = array[i]
    const li = document.createElement("li");
    const countryName = document.createTextNode(country);
    li.appendChild(countryName);
    ul1.appendChild(li);
}}


ul1.querySelectorAll('li').forEach(li => {
    li.addEventListener('click', (e) => {
        let selectdItem1 = e.target.innerText
        selectedData1.innerText = selectdItem1
        
        for (const li of document.querySelectorAll("li.selected")) {
            li.classList.remove("selected");
        }
        e.target.classList.add('selected')
        customInputContainer1.classList.toggle('show')
    })
});

function updateData1(data) {
    let selectedCountry = data.innerText
    selectedData1.innerText = selectedCountry

    for (const li of document.querySelectorAll("li.selected")) {
        li.classList.remove("selected");
    }
    data.classList.add('selected')
    customInputContainer1.classList.toggle('show')
    console.log(selectedCountry);
}

searchInput1.addEventListener('keyup', (e) => {
    let searchedVal = searchInput1.value.toLowerCase()
    let searched_country = []

    searched_country = array1.filter(data => {
        return data.toLocaleLowerCase().startsWith(searchedVal)
    }).map(data => {
        return `<li onClick="updateData1(this)">${data}</li>`
    }).join('')
    ul1.innerHTML = searched_country ? searched_country : "<p style='margin-top: 1rem;'>Opps can't find any result <p style='margin-top: .2rem; font-size: .9rem;'>Try searching something else.</p></p>"
})












// --------------------- Created By InCoder ---------------------
let customInput2 = document.querySelector('.customInput2')
selectedData2 = document.querySelector('.selectedData2')
searchInput2 = document.querySelector('.searchInput2 input')
ul2 = document.querySelector('.options2 .ul2')
customInputContainer2 = document.querySelector('.customInputContainer2')

window.addEventListener('click', (e) => {
    if (document.querySelector('.searchInput2').contains(e.target)) {
        document.querySelector('.searchInput2').classList.add('focus')
    } else {
        document.querySelector('.searchInput2').classList.remove('focus')
    }
})

var array2 = [
    "Custom Input",
    "Mali",
    "Vanuatu",
    "Venezuela",
    "Viet Nam",
    "Virgin Islands, British",
    "Virgin Islands, U.s.",
    "Wallis and Futuna",
    "Western Sahara",
    "Yemen",
    "Zambia",
    "Zimbabwe"
];

customInput2.addEventListener('click', () => {
    customInputContainer2.classList.toggle('show')
})

let array2Length = array2.length

for (let i = 0; i < array2Length; i++) {
    let country = array2[i]
    const li = document.createElement("li");
    const countryName = document.createTextNode(country);
    li.appendChild(countryName);
    ul2.appendChild(li);
}


ul2.querySelectorAll('li').forEach(li => {
    li.addEventListener('click', (e) => {
        let selectdItem2 = e.target.innerText
        selectedData2.innerText = selectdItem2
        
        for (const li of document.querySelectorAll("li.selected")) {
            li.classList.remove("selected");
        }
        e.target.classList.add('selected')
        customInputContainer2.classList.toggle('show')
    })
});

function updateData2(data) {
    let selectedCountry = data.innerText
    selectedData2.innerText = selectedCountry

    for (const li of document.querySelectorAll("li.selected")) {
        li.classList.remove("selected");
    }
    data.classList.add('selected')
    customInputContainer2.classList.toggle('show')
    console.log(selectedCountry);
}

searchInput2.addEventListener('keyup', (e) => {
    let searchedVal = searchInput2.value.toLowerCase()
    let searched_country = []

    searched_country = array2.filter(data => {
        return data.toLocaleLowerCase().startsWith(searchedVal)
    }).map(data => {
        return `<li onClick="updateData2(this)">${data}</li>`
    }).join('')
    ul2.innerHTML = searched_country ? searched_country : "<p style='margin-top: 1rem;'>Opps can't find any result <p style='margin-top: .2rem; font-size: .9rem;'>Try searching something else.</p></p>"
})