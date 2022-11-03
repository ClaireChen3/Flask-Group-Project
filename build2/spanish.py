const options = {
    method: 'GET',
    headers: {
        'X-RapidAPI-Key': '721c8e8789msh4f6199095fcff35p13f037jsnc1e7998c8457',
        'X-RapidAPI-Host': 'spotify81.p.rapidapi.com'
    }
};

fetch('https://spotify81.p.rapidapi.com/top_200_tracks', options)
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(err => console.error(err));