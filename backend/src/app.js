// modulok importalasa
const express = require('express');
// bodyParser segit feldolgozni json fileokat konnyen
const bodyParser = require('body-parser');
const morgan = require('morgan');
const cors = require('cors');
const mysql = require('mysql');
const config = require('./config/config');

// felepeti az express servert
const app = express();
// combined-al megjelenit meta-informaciokat a reqestet feladorol
app.use(morgan('combined'));
app.use(bodyParser.json());
app.use(cors());

/*Fobb express reqek: get, post, put, patch, delete, stb... */
const connection = mysql.createConnection({
    host: config.db.host,
    user: config.db.user,
    password: config.db.password,
    database: config.db.database,
});


connection.connect(function (err) {
    if (err) throw err;
    console.log("Connected!");
});

app.post('/verification', function (req, res) {
    var sql = `SELECT id from user where (username = "${req.body.name}" && password="${req.body.password}")`;
    connection.query(sql, function (err, result, fields) {
        console.log(result[0]);
        if (!result[0]) {
            res.send({
                error: 'Wrong username or password!'
            })
            console.log('Wrong username or password!');
            return;
        } else {

            res.send({
                message: `User ${req.body.name} logged in!`
            })
            console.log(`User ${req.body.name} logged in!`);
        }
    });
});

app.post('/register', function (req, res) {
    var sql = `INSERT INTO user (username,last_name ,first_name, birth_date, profile_picture, created_at, gender, password, email_addres, phone_number, deposit) VALUES ( "${req.body.name}", "Kolompár" , "Kárlosz","${req.body.date}", 'kep', CURDATE(), "${req.body.gender}", "${req.body.password}", "${req.body.email}", "${req.body.phonenumber}", 0)`;
    connection.query(sql, function (err, result) {
        if (err) {
            res.send({
                error: 'Registration rejected! User data already in use!'
            })
            console.log('Registration rejected! User data already in use!');
            return;
        } else {

            res.send({
                message: `User ${req.body.name} registered! Have fun!`
            })
            console.log(`User ${req.body.name} registered! Have fun!`);
        }
    });
});

app.post('/changedeposit', function(req,res){
    var sql = `SELECT id from user where  password="${req.body.password}"`;
    connection.query(sql, function(err, result){
        if (err){
            res.send({
                error: 'Wrong password!'
            })
            console.log('Wrong password!');
            return;
        } else{
            var sql1 = `UPDATE user SET deposit = "${req.body.deposit}" WHERE (id = "${result[0].id}");`
            connection.query(sql1, function (err1) {
                if(err1){
                    res.send({
                        error: 'Wrong update!'
                    })
                }else{
                    res.send({
                        message: "Successful update"
                    })
                    console.log('Successful update');
                }
            })
        }
    });
});

app.post('/changepassword', function(req,res){
    var sql = `SELECT id from user where  password="${req.body.password}"`;
    connection.query(sql, function(err, result){
        if (err){
            res.send({
                error: 'Wrong password!'
            })
            console.log('Wrong password!');
            return;
        } else{
            var sql1 = `UPDATE user SET password = "${req.body.new_password}" WHERE (id = "${result[0].id}");`
            connection.query(sql1, function (err1) {
                if(err1){
                    res.send({
                        error: 'Wrong update!'
                    })
                }else{
                    res.send({
                        message: "Successful update"
                    })
                    console.log('Successful update');
                }
            })
        }
    });
});

const getUserInfo = (id) => {
    return new Promise((resolve, reject) => {
        connection.query(`SELECT * from user where id = "${id}"`, function (error, results, fields) {
            if (error) { reject(error) }
            else { resolve(results[0]) }
            console.log(results[0]);
        });
    })
}

app.get('/user/:id', async (req, res) => {
    user = await getUserInfo(req.params.id).catch(err => console.error(err))
    var day = user.birth_date.getDate();
    var month = user.birth_date.getMonth();
    var year = user.birth_date.getFullYear();
    user.birth_date = year + '-' + month + '-' + day;

    var day = user.created_at.getDate();
    var month = user.created_at.getMonth();
    var year = user.created_at.getFullYear();
    user.created_at = year + '-' + month + '-' + day;

    console.log(user);
    res.send(user);
});

app.get('/', (req, res) => {
    console.log('Someone connected!');
    res.send({ message: 'Hello bello te lo' });
});

//require('./routes')(app)

app.listen(config.port, function () {
    console.log(`Server is listening on port ${config.port}`);
});