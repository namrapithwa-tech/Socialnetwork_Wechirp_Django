function commentReplayToggle(parent_id){
    const row = document.getElementById(parent_id);
    if (row.classList.contains('d-none'))
    {
        row.classList.remove('d-none');
    }
    else
    {
        row.classList.add('d-none');
    }
}   
function shareToggle(parent_id){
    const row = document.getElementById(parent_id);
    if (row.classList.contains('d-none'))
    {
        row.classList.remove('d-none');
    }
    else
    {
        row.classList.add('d-none');
    }
}   
function showNotification(){
    const container = document.getElementById('notification-container');
    if (container.classList.contains('d-none'))
    {
        container.classList.remove('d-none');
    }
    else
    {
        container.classList.add('d-none');
    }
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function removenotification(removeNotificationURL,redirectURL){
    const csrftoken = getCookie('csrftoken');
    let xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function()
    {
        if(xmlhttp.readyState == XMLHttpRequest.DONE)
        {
            if(xmlhttp.status == 200)
            {
                windows.location.replace(redirectURL);
            }
            else
            {
                alert('Thre was an error...!!');
            }
        } 
    };
    xmlhttp.open("delete",removeNotificationURL,true);
    xmlhttp.setRequestHeader("X-CSRFToken",csrftoken);
    xmlhttp.send();
    
}

function formattags()
{   
    
    const elements=document.getElementsByClassName('tag');

    for (let i=0;i<elements.length;i++) {
        let bodyText = elements[i].children[0].innerText;
        let words = bodyText.split(' ');

        for(let j=0;j<words.length;j++)
        {
            if(words[j][0] === '#'){
                let replacedText = bodyText.replace(/\s\#(.*?)(\s|$)/g, `<a href="/social/explore?query=${words[j].substring(1)}"> ${ words[j] }</a>`);
                elements[i].innerHTML = replacedText;
            }
        }
    }
}
formattags();