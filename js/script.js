url = 'https://harshitkumar9030-super-potato-67qrvq97wwrfj9p-5000.preview.app.github.dev'

//dont put '/' at the end of url

form_submit = document.getElementById("add_template")

form_submit.onsubmit = async (e) => {
    e.preventDefault()
    let form_data = new FormData(form_submit)
    let data = {}
    for (let [key, value] of form_data.entries()) {
        data[key] = value
    }
    if(data['template-name'] == "" || data['template-subject'] == "" || data['template-body'] == ""){
        alert('Please enter info.')
        return
    }
    else{
        alert('Template added successfully')

        let response = await fetch(url + '/api/add_template/', {
            method: 'POST',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin':'*'
            },
            body: JSON.stringify(data)
        })
        let result = await response.json()
        console.log(result)        
    }
}
