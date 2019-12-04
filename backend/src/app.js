//python import
const child_process = require('child_process')

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
                message: `${result[0].id}`
            })
            console.log(`User ${req.body.name} logged in!`);
        }
    });
});

app.post('/register', function (req, res) {
    var sqlinsertuser = `INSERT INTO user (username, last_name ,first_name, birth_date, profile_picture, created_at, gender, password, email_addres, phone_number) VALUES ( "${req.body.name}" , "${req.body.lastname}","${req.body.firstname}","${req.body.birth_date}", "https://eu.ui-avatars.com/api/?background=fff&color=4caf50&bold=true&name=${req.body.firstname}+${req.body.lastname}", CURDATE(), "${req.body.gender}", "${req.body.password}", "${req.body.email}", "${req.body.phonenumber}")`;
    connection.query(sqlinsertuser, function (err, result) {
        if (err) {
            res.send({
                error: 'Registration rejected! User data already in use!'
            })
            console.log('Registration rejected! User data already in use!');
            return;
        } else {


            var sqlgetuserid = `SELECT id from user where username = "${req.body.name}"`
            connection.query(sqlgetuserid, function (err, result) {
                var sqlinsertdeposit = `INSERT INTO deposit (user_id) VALUES ('${result[0].id}');`
                connection.query(sqlinsertdeposit, function (err, result) {
                    if (err) {
                        res.send({
                            error: 'Registration rejected! Deposit creation failed!'
                        })
                        console.log('Registration rejected! Deposit creation failed!');
                        return;
                    } else {
                        res.send({
                            message: `User ${req.body.name} registered! Have fun!`
                        })
                        console.log(`User ${req.body.name} registered! Have fun!`);
                    }
                });
            });
        }
    });
});

app.post('/changedeposit', function (req, res) {
    var sql = `UPDATE deposit SET ${req.body.currency} = "${req.body.new_deposit}" WHERE user_id="${req.body.id}"`
    connection.query(sql, function (err) {
        if (err) {
            res.send({
                error: 'Deposit update error!'
            })
        } else {
            res.send({
                message: "Successful deposit update!"
            })
        }
    });

});

app.post('/changepassword', function (req, res) {
    var sql = `UPDATE user SET password = "${req.body.new_password}" WHERE id="${req.body.id}"`;
    connection.query(sql, function (err) {
        if (err) {
            res.send({
                error: 'Password change error!'
            })
        } else {
            res.send({
                message: "Successful password update"
            })
        }
    })
});

const getDeposit = (id) => {
    return new Promise((resolve, reject) => {
        connection.query(`SELECT ron, gbp, usd, eur from deposit where user_id = "${id}"`, function (error, results, fields) {
            if (error) { reject(error) }
            else { resolve(results[0]) }
            console.log(results[0]);
        });
    })
}
app.get('/cards/:id', async (req, res) => {
    amounts = await getDeposit(req.params.id).catch(err => console.error(err))
    var deposit = [
        {
            currency: "RON",
            amount: amounts.ron,
            sign: "",
            icon: "RON",
            from_curreny: "RON",
            exchange: "4.29"
        },
        {
            currency: "Euro",
            amount: amounts.eur,
            sign: "€",
            icon: "fas fa-euro-sign",
            from_curreny: "RON",
            exchange: "4.76"
        },
        {
            currency: "GBP",
            amount: amounts.gbp,
            sign: "£",
            icon: "fas fa-pound-sign",
            from_curreny: "RON",
            exchange: "5.50"
        },
        {
            currency: "USD",
            amount: amounts.usd,
            sign: "$",
            icon: "fas fa-dollar-sign",
            from_curreny: "RON",
            exchange: "4.29"
        }
    ];

    console.log(deposit);
    res.send(deposit);
})

app.get('/deposit/:id', async (req, res) => {
    deposit = await getDeposit(req.params.id).catch(err => console.error(err))
    console.log(deposit);
    res.send(deposit);
})


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
    var month = user.birth_date.getMonth() + 1;
    var year = user.birth_date.getFullYear();
    user.birth_date = year + '-' + month + '-' + day;
    var day = user.created_at.getDate();
    var month = user.created_at.getMonth() + 1;
    var year = user.created_at.getFullYear();
    user.created_at = year + '-' + month + '-' + day;
    res.send(user);
});

app.get('/statisticIncome/:id', async (req, res) => {
    sql = `select amount,date from transactions t join income i on t.id = i.transaction_id where date BETWEEN NOW() - INTERVAL 30 DAY AND NOW() and user_id = "${req.params.id}";`
    connection.query(sql, function (err, result) {
        if (err) {
            res.send({
                error: 'Wrong statisticIncome'
            })
        } else {
            for (let index = 0; index < result.length; index++) {
                result[index].date = result[index].date.getTime();
            }
            res.send(result);
        }
    });
});

app.get('/statisticExpense/:id', async (req, res) => {
    sql = `select amount,date from transactions t join expense e on t.id = e.transaction_id where date BETWEEN NOW() - INTERVAL 30 DAY AND NOW() and user_id = "${req.params.id}";`
    connection.query(sql, function (err, result) {
        if (err) {
            res.send({
                error: 'Wrong statisticExpense'
            })
        } else {
            for (let index = 0; index < result.length; index++) {
                result[index].date = result[index].date.getTime();
            }
            res.send(result);
        }
    });
});

app.get('/statisticExchangeNumber/:id', async (req, res) => {
    sql = `select count(*) as number, date from exchange  where date BETWEEN NOW() - INTERVAL 30 DAY AND NOW() and user_id = "${req.params.id}" group by date;`
    connection.query(sql, function (err, result) {
        if (err) {
            res.send({
                error: "Wrong statisticExchangeNumber"
            })
        } else {
            for (let index = 0; index < result.length; index++) {
                result[index].date = result[index].date.getTime();
            }
            res.send(result);
        }
    });
});

app.get('/statisticValuta/:valuta', async (req, res) => {
    sql = `select web_address,currency,purchase_price from valuta`;
    connection.query(sql, function (err, result) {
        if (err) {
            error: 'Wrong getvaluta'
        } else {
            res.send(result);
        }
    });
});

app.get('/', (req, res) => {
    console.log('Someone connected!');
    res.send({ message: 'Hello bello te lo' });
});

//require('./routes')(app)

app.listen(config.port, function () {
    console.log(`Server is listening on port ${config.port}`);
});

function python_run() {
    const runscript = child_process.exec("python ..\\datacollector\\main.py", { timeout: 10 * 1000 })
    runscript.stdout.on('data', d => console.log(d))
    runscript.on("error", err => console.log(err))
    runscript.on("exit", () => {
        console.log("Python code runed")
    })
}
python_run();
setInterval(() => python_run(), 100 * 1000);
