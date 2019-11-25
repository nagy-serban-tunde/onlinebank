// modulok importalasa
const express = require('express');
// bodyParser segit feldolgozni json fileokat konnyen
const bodyParser = require('body-parser');
const morgan = require('morgan');
const cors = require('cors');

//mysql connection

var mysql = require('mysql');
//native password
//ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'
var con = mysql.createConnection({
  host: "127.0.0.1",
  user: "root",
  password: "diak123",
  database : 'online_bank'
});

const getUser = (id) => {
    return new Promise((resolve, reject) => {
        con.query(`SELECT * from user where id = "${id}"`, function (error, results, fields) {
        if (error) { reject(error) }
        else { resolve(results[0]) }
            //console.log('The solution is: ', results[0]);
        });
    })
}

con.connect(function(err) {
  if (err) throw err;
  console.log("Connected!");
});

/*Fobb express requestek: get, post, put, patch, delete, stb... */

// felepeti az express servert
const app = express();
// combined-al megjelenit meta-informaciokat a reqestet feladorol
app.use(morgan('combined'));
app.use(bodyParser.json());
app.use(cors());

app.get('/user/:id', async (request, response) => {
    user = await getUser(request.params.id).catch(err => console.error(err))
    console.log(user);
    response.send(user);
});

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