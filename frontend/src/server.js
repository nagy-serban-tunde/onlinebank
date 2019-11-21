// modulok importalasa
const mysql = require('mysql');
// express server fogja tovabbitani az adatokat
const express = require('express');
// bodyParser segit feldolgozni json fileokat konnyen
const bodyParser = require('body-parser');
const morgan = require('morgan');

/*Fobb express requestek: get, post, put, patch, delete, stb... */

// felepeti az express servert
const app = express();
// combined-al megjelenit meta-informaciokat a reqestet feladorol
//app.use(morgan('combined'));
app.use(bodyParser.json());


var connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'diak123',
    database: 'online_bank'
});

connection.connect((error) => {
    if (error) {
        console.log('Error on server-database connection!\n' + error);
    }
    else {
        console.log('Server succesfully connected to MySQL database!\n');
    }
});

app.get('/', function (request, response) {
    console.log('Someone connected!');
    response.send({ message: 'Hello bello te lo' });
});

app.get('/querry', function (request, response) {
    console.log('GET request recieved');
    //cucc
    connection.query("SELECT * FROM valamitable", function (error, rows, fields) {
        if (error) {
            console.log('ERROR in the querry!\n' + error);
        }
        else {
            console.log('Querry succesfull!');
            console.log(rows);
        }
        // Callback function
    });
});


app.post('/test', function (request, response) {
    console.log('POST request recieved');
});

app.listen(8081, function () {
    console.log("Server is listening on port 8081");
});
