// modulok importalasa
const express = require('express');
// bodyParser segit feldolgozni json fileokat konnyen
const bodyParser = require('body-parser');
const morgan = require('morgan');
const cors = require('cors');

/*Fobb express requestek: get, post, put, patch, delete, stb... */

// felepeti az express servert
const app = express();
// combined-al megjelenit meta-informaciokat a reqestet feladorol
app.use(morgan('combined'));
app.use(bodyParser.json());
app.use(cors());

app.get('/', (request, response) => {
    console.log('Someone connected!');
    response.send({ message: 'Hello bello te lo' });
});

app.post('/register', (request, response) => {
    console.log('POST request received!');
    response.send({
        message: `User ${request.body.name} registered! Have fun!`
    })
})

app.listen(8081, function () {
    console.log("Server is listening on port 8081");
});