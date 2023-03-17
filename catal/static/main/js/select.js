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


// preparation brands
$.ajax('brands', {
    dataType: 'json', type: 'GET', success: (res) => {
        let array = res['list']
        getListOne(array);
    }
})

function getListOne(array) {
    arrayLength = array.length
    for (let i = 0; i < arrayLength; i++) {
        let country = array[i]
        const li = document.createElement("li");
        const countryName = document.createTextNode(country);
        li.appendChild(countryName);
        ul1.appendChild(li);
    }
    querySelector();

}


customInput1.addEventListener('click', () => {
    customInputContainer1.classList.toggle('show')
})


function querySelector() {
    ul1.querySelectorAll('li').forEach(li => {
        li.addEventListener('click', (e) => {
            selectedData1.innerText = e.target.innerText
            updateListTwo(selectedData1.innerText);
            for (const li of document.querySelectorAll("li.selected")) {
                li.classList.remove("selected");
            }
            e.target.classList.add('selected')
            customInputContainer1.classList.toggle('show')
        })
    });
}


// if you select brand it will change the list of marks
function updateListTwo(element) {
    let array = sorted_list[element]
    getListTwo(array);
}


// preparation all marks
$.ajax('marks_unsorted', {
    dataType: 'json', type: 'GET', success: (res) => {
        let listMarks = res['list']
        getListTwo(listMarks);
    }
})

function querySelectorTwo() {
    ul2.querySelectorAll('li').forEach(li => {
        li.addEventListener('click', (e) => {
            selectedData2.innerText = e.target.innerText

            for (const li of document.querySelectorAll("li.selected")) {
                li.classList.remove("selected");
            }
            e.target.classList.add('selected')
            customInputContainer2.classList.toggle('show')
        })
    });
}

let sorted_list = []
// preparation marks for each brand
$.ajax('marks_sorted', {
    dataType: 'json', type: 'GET', success: (res) => {
        sorted_list = res['list']
    }
})

function getListTwo(array) {
    while (ul2.firstChild) {
        ul2.removeChild(ul2.firstChild);
    }
    let arrayLength = array.length
    for (let i = 0; i < arrayLength; i++) {
        let country = array[i]
        const li = document.createElement("li");
        const countryName = document.createTextNode(country);
        li.appendChild(countryName);
        ul2.appendChild(li);
    }
    querySelectorTwo();
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

customInput2.addEventListener('click', () => {
    customInputContainer2.classList.toggle('show')
})

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